from pathlib import Path
from yaml import safe_load
from pydantic import BaseModel


ROOT_DIR = Path(__name__).absolute().parent
BASE_DIR = ROOT_DIR / "src"


class PathConfig(BaseModel):
    """Schema for Filepaths."""

    train_data: str
    test_data: str
    model_path: str


class ModelConfig(BaseModel):
    """Schema for the model variables."""

    test_size: float
    random_state: int
    target: str
    num_vars: list[str]
    discrete_vars: list[str]
    cat_vars: list[str]
    num_vars_wf_na: list[str]
    cat_vars_wf_na: list[str]
    features_to_drop: list[str]


class Config(BaseModel):
    """Configuratiion for the Project."""

    path_config: PathConfig
    model_config: ModelConfig


def load_yaml_config(*, filepath: Path = None) -> dict:
    """This is used to load the configuration file as a dict
    
    Params:
        filepath (Path): Config filepath in yaml/yml.

    Returns:
        config_file (dict): The loaded config.
    """
    if filepath is None:
        filepath = BASE_DIR / "config.yml"

    with open(filepath, "r", encoding="utf-8") as file:
        config_file = safe_load(file)
        return config_file


def parse_config(*, filepath: Path) -> Config:
    """This is used to validate the configuration used in the project.
    
    Params:
        filepath (Path): Config filepath in yaml/yml.

    Returns:
        config (Config): The validated config object.
    """
    _config_file = load_yaml_config(filepath=filepath)
    config = Config(
        path_config=PathConfig(**_config_file), model_config=ModelConfig(**_config_file)
    )
    return config

config = parse_config(filepath=None)

