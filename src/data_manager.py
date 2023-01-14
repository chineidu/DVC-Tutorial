"""
This module is used for loading and manipulating the data.
"""

import warnings

import pandas as pd

warnings.filterwarnings("ignore")
import logging
import typing as tp

from sklearn.base import BaseEstimator, TransformerMixin


# Helper Functions
def set_up_logger(delim: str = "::") -> tp.Any:
    """This is used to create a basic logger."""
    format_ = f"[%(levelname)s] {delim} %(asctime)s {delim} %(message)s"
    logging.basicConfig(level=logging.INFO, format=format_)
    logger = logging.getLogger(__name__)
    return logger


logger = set_up_logger()


def load_data(*, filepath: str) -> pd.DataFrame:
    """This is used to load data as a dataframe.

    Params:
        filepath (str): The filepath of the input data.

    Returns:
        df (pd.Dataframe): A DF containing the input data.
    """
    _logger = set_up_logger()
    df = pd.read_csv(filepath)
    _logger.info(f"Shape of df: {df.shape}\n")
    return df


class CastVariables(BaseEstimator, TransformerMixin):
    """This is used to convert numerical variables to
    categorical variables."""

    def __init__(self, features: list[str]) -> None:
        self.features = features

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame, y=None) -> pd.DataFrame:
        X = X.copy()
        # Cast the features
        X[self.features] = X[self.features].astype(str)
        return X

