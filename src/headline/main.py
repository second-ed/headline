import logging

from headline.io import get_matching_files
from headline.transform import sort_src_funcs_and_tests

from ._logger import (
    compress_logging_value,
    is_logging_enabled,
    setup_logger,
)

if is_logging_enabled(__file__):
    setup_logger(__file__, 2)

logger = logging.getLogger()


def main(
    current_dir: str,
    inp_sort_type: str,
    inp_tests_only: bool,
    inp_rename: bool,
) -> None:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    matching_files = get_matching_files(current_dir)

    for src, tests in matching_files:
        sort_src_funcs_and_tests(
            src, tests, inp_sort_type, inp_tests_only, inp_rename
        )
