import logging

from headline.io import get_matching_files
from headline.transform import sort_src_funcs_and_tests

from ._logger import (
    compress_logging_value,
    is_logging_enabled,
    setup_logger,
)

if is_logging_enabled():
    setup_logger(__file__, 2)

logger = logging.getLogger()


def main_process(
    cwd: str,
    src_dir: str,
    tests_dir: str,
    sort_type: str,
    tests_only: bool,
    rename: bool,
    suffix: str,
):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    paths = get_matching_files(cwd, src_dir, tests_dir)

    for src_path, test_path in paths:
        sort_src_funcs_and_tests(
            src_path,
            test_path,
            sort_type,
            tests_only,
            rename,
            suffix,
        )
