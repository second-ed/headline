import glob
import os
from typing import List

from headline.utils import strip_test_prefix_suffix


def get_src_code(path: str) -> str:
    with open(path, "r") as f:
        src_code = f.read()
    return src_code


def save_modified_code(modified_code: str, filepath: str) -> bool:
    with open(filepath, "w") as f:
        f.write(modified_code)
    return True


def find_files_in_folders(
    all_files: List[str], search_folders: List[str]
) -> List[str]:
    return [
        f
        for f in all_files
        if any([s for s in search_folders if s in os.path.dirname(f)])
    ]


def find_matching_files(
    src_files: List[str], test_files: List[str]
) -> List[str]:
    matching_files = []

    for f in src_files:
        for f2 in test_files:
            base_f = os.path.basename(f)
            base_f2 = os.path.basename(f2)
            if base_f == "__init__.py" or base_f2 == "__init__.py":
                continue
            if base_f.strip("_") == strip_test_prefix_suffix(base_f2):
                matching_files.append((f, f2))

    return matching_files


def get_matching_files(current_location: str):
    all_files = glob.glob(f"{current_location}/**/**.py", recursive=True)
    src_files = find_files_in_folders(all_files, ["src"])
    test_files = find_files_in_folders(all_files, ["tests"])
    matching_files = find_matching_files(src_files, test_files)
    return matching_files
