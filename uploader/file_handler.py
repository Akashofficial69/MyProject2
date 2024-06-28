import os
import glob


def get_files(directory):
    file_types = {
        "images": ["jpg", "png", "svg", "webp"],
        "media": ["mp3", "mp4", "mpeg4", "wmv", "3gp", "webm"],
        "documents": ["doc", "docx", "csv", "pdf"]
    }
    files = {"images": [], "media": [], "documents": []}

    for file_type, extensions in file_types.items():
        for ext in extensions:
            files[file_type].extend(glob.glob(os.path.join(directory, '**', f'*.{ext}'), recursive=True))

    return files
