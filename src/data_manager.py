"""
This module is used for loading and manipulating the data.
"""

import warnings

import pandas as pd
from pathlib import Path

warnings.filterwarnings("ignore")
import logging
import joblib
import typing as tp

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.utilities import TRAINED_MODELS_FILEPATH


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


def split_into_features_n_target(*, data: pd.DataFrame, target: str) -> tp.Tuple:
    """Split the data into independentand dependent features.

    Params:
        data (pd.DataFrame): DF containing the training data.
        target (int): The dependent feature.

    Returns:
        X, y (Tuple): The independent and dependent features respectively.
    """
    if target in data.columns:
        X = data.drop(columns=[target])
        y = data[target]
    else:
        raise NotImplementedError("Unsupported Dataframe")
    return (X, y)


def split_train_data(
    *, data: pd.DataFrame, target: str, test_size: float, random_state: int
) -> tp.Tuple:
    """This returns a split training data containing the
    X_train, X_validate, y_train and y_validate

    Params:
        data (pd.DataFrame): DF containing the training data.
        target (int): The dependent feature.
        test_size (float): The proportion of the data to include in the test split.
        random_state (int): Controls the shuffling applied and ensures reproducibility.

    Returns:
        X_train, X_validate, y_train and y_validate (tuple):
            A tuple containing the training and validation sets.
    """
    X, y = split_into_features_n_target(data=data, target=target)

    X_train, X_validate, y_train, y_validate = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return (X_train, X_validate, y_train, y_validate)


def save_model(*, filename: tp.Union[str, Path], pipe: Pipeline) -> None:
    """This is used to persit a model.
    Params:
    -------
    filename (Path): Filepath to save the data.
    Returns:
    --------
    None
    """
    filename = TRAINED_MODELS_FILEPATH / filename

    logger.info("Saving Model ...")
    with open(filename, "wb") as file:
        joblib.dump(pipe, file)


def load_model(*, filename: tp.Union[str, Path]) -> tp.Any:
    """This is used to load the trained model."""
    filename = TRAINED_MODELS_FILEPATH / filename
    logger.info("Loading Model ...")
    with open(filename, "rb") as file:
        trained_model = joblib.load(filename=file)
    return trained_model


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
