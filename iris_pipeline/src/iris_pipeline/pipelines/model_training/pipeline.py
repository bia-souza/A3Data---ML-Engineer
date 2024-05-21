from kedro.pipeline import Pipeline, node
from .nodes import ModelTrainer

def create_pipeline(**kwargs):
    model_trainer = ModelTrainer()
    return Pipeline(
        [
            node(func=model_trainer.train_model, inputs=["X_train", "y_train"], outputs="model"),
            node(func=model_trainer.evaluate_model, inputs=["model","X_test", "y_test"], outputs="accuracy"),
            node(func=model_trainer.save_model, inputs=["model", "params:model_filepath"], outputs=None),
        ]
    )
