import os
from typing import List


def discover_files(file_path: object=__file__) -> List:
    cwd = os.path.dirname(file_path)
    submodules = []
    for root, dirs, files in os.walk(cwd):
        for filename in files:
            submodules.append(filename if not filename.startswith('__') and \
                                          not filename.endswith('.pyc') else None)
    return [sub.rstrip('.py') for sub in submodules if sub]


def discover_folders(file_path: object=__file__) -> List:
    cwd = os.path.dirname(file_path)
    submodules = []
    for root, dirs, files in os.walk(cwd):
        for folder in dirs:
            submodules.append(folder if not folder.startswith('__') else None)
    return [sub for sub in submodules if sub]
