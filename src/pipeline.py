import warnings

from feature_engine.encoding import OrdinalEncoder, RareLabelEncoder
from feature_engine.imputation import CategoricalImputer, MeanMedianImputer
from feature_engine.selection import DropFeatures
from feature_engine.transformation import YeoJohnsonTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# custom imports
from src import config
from src.data_manager import CastVariables

pipe = Pipeline(
    steps=[
        # Replace the missing values in numerical variables
        (
            "mean_imputer",
            MeanMedianImputer(
                imputation_method="median", variables=config.model_config.num_vars_wf_na
            ),
        ),
        # Cast the numerical variables
        (
            "cast_feats",
            CastVariables(features=config.model_config.discrete_vars),
        ),
        # Encode Rare Labels
        (
            "rare_label_enc",
            RareLabelEncoder(
                tol=0.05,
                n_categories=5,
                variables=config.model_config.discrete_vars,
            ),
        ),
        # Transform the variables
        (
            "yea_johnson_transf",
            YeoJohnsonTransformer(variables=config.model_config.num_vars),
        ),
        # Drop variable(s)
        (
            "drop_feats",
            DropFeatures(features_to_drop=config.model_config.features_to_drop),
        ),
        # Replace the missing values in categorical variables
        (
            "cat_vars_wf_na",
            CategoricalImputer(
                imputation_method="frequent", variables=config.model_config.cat_vars_wf_na
            ),
        ),
        # Encode Categorical Variables
        (
            "cat_enc",
            OrdinalEncoder(
                encoding_method="ordered",
                variables=config.model_config.cat_vars
                + config.model_config.discrete_vars,
            ),
        ),
        # Scale the  variables
        (
            "scaler",
            StandardScaler(),
        ),
        # Estimator
        (
            "random_forest_classifier",
            RandomForestClassifier(
                n_estimators=config.model_config.n_estimators,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
