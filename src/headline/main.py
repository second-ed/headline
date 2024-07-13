# import logging
# from src.headline.config import Config
# from src.headline._logger import (
#     get_dir_path,
#     setup_logger,
# )

# Config().set_filepath(get_dir_path(__file__, 2, "configs/example_config.yaml"))

# setup_logger(__file__, 2)
# logger = logging.getLogger()


from headline.io import get_matching_files
from headline.transform import sort_src_funcs_and_tests


def main(current_dir, inp_sort_type: str, inp_tests_only: bool) -> None:
    matching_files = get_matching_files(current_dir)

    for src, tests in matching_files:
        sort_src_funcs_and_tests(src, tests, inp_sort_type, inp_tests_only)
