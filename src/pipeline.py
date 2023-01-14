from feature_engine.encoding import OrdinalEncoder
from feature_engine.encoding import RareLabelEncoder
from feature_engine.imputation import CategoricalImputer
from feature_engine.imputation import MeanMedianImputer
from feature_engine.selection import DropFeatures
from feature_engine.transformation import YeoJohnsonTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore")

# custom imports
from src import config


pipe = Pipeline(
    steps=[
        # Replace the missing values in numerical variables
        (
            "mean_imputer",
            MeanMedianImputer(
                imputation_method="median", variables=config.model_config.num_vars_wf_na
            ),
        ),
        
    ]
)
