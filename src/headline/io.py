import glob
import logging
import os
from typing import List, Tuple

from headline.utils import format_code_str, strip_test_prefix_suffix

from ._logger import compress_logging_value

logger = logging.getLogger()


def get_src_code(path: str) -> str:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    with open(path, "r") as f:
        src_code = f.read()
    return src_code


def save_modified_code(
    modified_code: str, filepath: str, format_code: bool = True
) -> bool:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    if format_code:
        modified_code = format_code_str(modified_code)
    with open(filepath, "w") as f:
        f.write(modified_code)
    return True


def find_files_in_folders(
    all_files: List[str], search_folders: List[str]
) -> List[str]:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    return [
        f
        for f in all_files
        if any([s for s in search_folders if s in os.path.dirname(f)])
    ]


def find_matching_files(
    src_files: List[str], test_files: List[str]
) -> List[Tuple[str, str]]:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    matching_files, matched = [], []

    for f in src_files:
        for f2 in test_files:
            base_f = os.path.basename(f)
            base_f2 = os.path.basename(f2)
            if base_f == "__init__.py":
                matched.append(f)
                continue
            if base_f2 == "__init__.py":
                matched.append(f2)
                continue
            if base_f.strip("_") == strip_test_prefix_suffix(base_f2):
                matching_files.append((f, f2))
                matched.extend([f, f2])

    for f in src_files + test_files:
        if f not in matched and f != "__init__.py":
            matching_files.append((f, None))

    return matching_files


def get_matching_files(
    current_location: str, src_folder: str = "src", test_folder: str = "tests"
) -> List[Tuple[str, str]]:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    all_files = glob.glob(f"{current_location}/**/**.py", recursive=True)
    src_files = find_files_in_folders(all_files, [src_folder])
    test_files = find_files_in_folders(all_files, [test_folder])
    matching_files = find_matching_files(src_files, test_files)
    return matching_files
