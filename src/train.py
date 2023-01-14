import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics

from src.pipeline import pipe
from src.data_manager import load_data, split_train_data, save_model
from src import config, logger


def train_model(*, train_data: pd.DataFrame) -> tuple:
    """This is used to train the model.

    Params:
        train_data (Pandas DF): DF containing the training data.

    Returns:
        pipe, y_validate, y_pred (Tuple): Tuple containing the
        trained_model_pipe, actual y and predicted y values.
    """

    target = target = config.model_config.target
    test_size = config.model_config.test_size
    random_state = config.model_config.random_state

    # Split the data
    X_train, X_validate, y_train, y_validate = split_train_data(
        data=train_data,
        target=target,
        test_size=test_size,
        random_state=random_state,
    )

    # Train Model
    pipe.fit(X_train, y_train)

    # Make predictions
    y_pred = pipe.predict(X_validate)
    return pipe, y_validate, y_pred


if __name__ == "__main__":  # pragma: no cover
    logger.info("Loading training data.")
    train_data = load_data(filename=config.path_config.train_data)

    logger.info("Training the model.")
    pipe, y_validate, y_pred = train_model(train_data=train_data)

    logger.info("Saving the model.")
    save_model(filename=config.path_config.model_path, pipe=pipe)

    logger.info("Evaluating the model.")
    clf_report = metrics.classification_report(y_true=y_validate, y_pred=y_pred)
    print(clf_report)
    conf_matrix = metrics.confusion_matrix(y_true=y_validate, y_pred=y_pred)
    print(conf_matrix)
