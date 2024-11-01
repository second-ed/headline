"""module level description"""

import re
from typing import Dict

import pandas as pd

def _check_extension(filepath: str) -> bool:
    """this is a docstring

    Args:
        filepath (str): the filepath to check

    Returns:
        bool: if the extension is valid
    """
    return bool(filepath)


def _clean_data(data: pd.DataFrame) -> pd.DataFrame:
    return data


def _filepath_exists(filepath: str) -> bool:
    return bool(filepath)


def main(filepath: str) -> bool:
    data = _read_data(filepath)
    data = _clean_data(data)
    data_dict = _transform_data(data)

    for key, value in data_dict.items():
        data_dict[key] = _rename_data(value)

    merged_data = _merge_data(data_dict)

    return _save_data(merged_data, filepath)


def _merge_data(data_dict: Dict) -> pd.DataFrame:
    # this is an inline comment that hopefully will stay
    data = pd.concat([v for v in data_dict.values()])
    return data


# this is a comment related to the function below
def _read_data(filepath: str) -> pd.DataFrame:
    if _check_extension(filepath):
        return pd.DataFrame({})
    raise FileNotFoundError


def _rename_data(value: pd.DataFrame) -> str:
    def _replacer(match) -> str:
        content = match.group(1)
        cleaned_content = " ".join(content.split())
        return f"({cleaned_content})"

    return re.sub(
        r"\((.*?)\)", _replacer, str(value.iloc[0, 0]), flags=re.DOTALL
    )


def _save_data(data: pd.DataFrame, filepath: str) -> bool:
    if _filepath_exists(filepath):
        return True
    return False


def _transform_data(data: pd.DataFrame) -> dict:
    def _transform() -> dict:
        return {"data": data}

    return _transform()


