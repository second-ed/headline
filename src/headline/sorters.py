import logging
from typing import List

from headline.visitors.func_visitors import FuncDef

from ._logger import compress_logging_value

logger = logging.getLogger()


def sort_funcs_newspaper(funcs: List[FuncDef], indent: int = 0) -> List[str]:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    sorted_funcs = sorted(
        funcs, key=lambda f: (len(f.called), -len(f.calls), f.name.strip("_"))
    )
    return [f.name for f in sorted_funcs if f.indent == indent]


def sort_funcs_calls(funcs: List[FuncDef], indent: int = 0) -> List[str]:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    sorted_funcs = sorted(funcs, key=lambda f: (-len(f.calls), f.name.strip("_")))
    return [f.name for f in sorted_funcs if f.indent == indent]


def sort_funcs_called(funcs: List[FuncDef], indent: int = 0) -> List[str]:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    sorted_funcs = sorted(funcs, key=lambda f: (-len(f.called), f.name.strip("_")))
    return [f.name for f in sorted_funcs if f.indent == indent]


def sort_funcs_alphabetical(funcs: List[FuncDef], indent: int = 0) -> List[str]:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    sorted_funcs = sorted(funcs, key=lambda f: f.name.strip("_"))
    return [f.name for f in sorted_funcs if f.indent == indent]


def sort_funcs_alphabetical_inc_leading_underscores(
    funcs: List[FuncDef], indent: int = 0
) -> List[str]:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    sorted_funcs = sorted(funcs, key=lambda f: f.name)
    return [f.name for f in sorted_funcs if f.indent == indent]
