"""module level description"""

import re

import pandas as pd


def main(filepath: str) -> bool:
    data = read_data(filepath)
    data = clean_data(data)
    data_dict = _transform_data(data)

    for key, value in data_dict.items():
        data_dict[key] = rename_data(value)

    merged_data = merge_data(data_dict)

    return save_data(merged_data, filepath)


# this is a comment related to the function below
def read_data(filepath: str) -> pd.DataFrame:
    if check_extension(filepath):
        return pd.DataFrame({})
    raise FileNotFoundError


def check_extension(filepath: str):
    """this is a docstring

    Args:
        filepath (str): the filepath to check

    Returns:
        bool: if the extension is valid
    """
    return True


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    return data


def _transform_data(data):
    def transform():
        return data

    return transform()


def rename_data(value):
    def replacer(match):
        content = match.group(1)
        cleaned_content = " ".join(content.split())
        return f"({cleaned_content})"

    return re.sub(r"\((.*?)\)", replacer, value, flags=re.DOTALL)


def merge_data(data_dict):
    # this is an inline comment that hopefully will stay
    data = pd.concat([v for v in data_dict.values()])
    return data


def save_data(data: pd.DataFrame, filepath: str) -> bool:
    if filepath_exists(filepath):
        return True
    return False


def filepath_exists(filepath: str):
    return True
