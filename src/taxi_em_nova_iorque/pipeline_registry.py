"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from taxi_em_nova_iorque.pipelines import transformacao, treino


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    pipeline_transformacao = transformacao.create_pipeline()
    pipeline_treino = treino.create_pipeline()

    return {
        "pipe_transformacao": pipeline_transformacao,
        "pipe_treino": pipeline_treino,
        "__default__": pipeline_transformacao + pipeline_treino,
    }
