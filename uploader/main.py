import configparser
import os

from uploader.aws import upload_to_s3
from uploader.gcs import upload_to_gcs
from uploader.file_handler import get_files


def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def main(config_file, directory):
    config = read_config(config_file)
    files = get_files(directory)

    for file in files['images'] + files['media']:
        upload_to_s3(file, config['AWS']['BucketName'])

    for file in files['documents']:
        upload_to_gcs(config['GCS']['BucketName'], file, os.path.basename(file))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python main.py <config_file> <directory>")
        sys.exit(1)

    config_file = sys.argv[1]
    directory = sys.argv[2]
    main(config_file, directory)
