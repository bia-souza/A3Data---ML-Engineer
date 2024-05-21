from iris_pipeline.pipelines.data_engineering import pipeline as de
from iris_pipeline.pipelines.model_training import pipeline as mt

def register_pipelines():
    data_engineering_pipeline = de.create_pipeline()
    model_training_pipeline = mt.create_pipeline()

    return {
        "de": data_engineering_pipeline,
        "mt": model_training_pipeline,
        "__default__": data_engineering_pipeline + model_training_pipeline
    }
