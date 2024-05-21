from kedro.pipeline import Pipeline, node
from .nodes import DataProcessor

def create_pipeline(**kwargs):
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" #kwargs['parameters']['url']
    data_processor = DataProcessor(url=url)
    return Pipeline(
        [
            node(func=data_processor.load_data, inputs=None, outputs="raw_data"),
            node(func=data_processor.preprocess_data, inputs="raw_data", outputs="preprocessed_data"),
            node(func=data_processor.split_data, inputs="preprocessed_data", outputs=["X_train", "X_test", "y_train", "y_test"]),
        ]
    )
