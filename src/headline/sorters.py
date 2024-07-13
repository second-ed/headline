import logging

from ._logger import compress_logging_value

logger = logging.getLogger()


def sort_funcs_newspaper(funcs):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    sorted_funcs = sorted(
        funcs, key=lambda f: (len(f.called), -len(f.calls), f.name.strip("_"))
    )
    return [f.name for f in sorted_funcs if f.indent == 0]


def sort_funcs_calls(funcs):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    sorted_funcs = sorted(
        funcs, key=lambda f: (-len(f.calls), f.name.strip("_"))
    )
    return [f.name for f in sorted_funcs if f.indent == 0]


def sort_funcs_called(funcs):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    sorted_funcs = sorted(
        funcs, key=lambda f: (-len(f.called), f.name.strip("_"))
    )
    return [f.name for f in sorted_funcs if f.indent == 0]


def sort_funcs_alphabetical(funcs):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    sorted_funcs = sorted(funcs, key=lambda f: f.name.strip("_"))
    return [f.name for f in sorted_funcs if f.indent == 0]


def sort_funcs_alphabetical_include_leading_underscores(funcs):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")
    sorted_funcs = sorted(funcs, key=lambda f: f.name)
    return [f.name for f in sorted_funcs if f.indent == 0]
