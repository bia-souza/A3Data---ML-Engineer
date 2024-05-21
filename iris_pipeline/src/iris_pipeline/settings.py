from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager

class ProjectContext(KedroContext):
    project_name = "iris_pipeline"
    project_version = "0.1"
    package_name = "iris_pipeline"

    def _get_pipelines(self):
        from .pipeline_registry import register_pipelines
        return register_pipelines()
