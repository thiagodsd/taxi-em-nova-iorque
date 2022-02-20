"""
This is a boilerplate pipeline 'treino'
generated using Kedro 0.17.6
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import split_data, otimiza_hiperparametros


def create_pipeline(**kwargs) -> Pipeline:
    r"""
    treino create_pipeline
    """
    pipeline_split_data = Pipeline(
        [
            node(
                split_data,
                inputs="treino_final",
                outputs=dict(
                    Xt="Xt",
                    yt="yt",
                    Xh="Xh",
                    yh="yh"
                ),
                name="node_treino_split_data",
            )
        ]
    )

    pipeline_otimiza_hiperparametros = Pipeline(
        [
            node(
                otimiza_hiperparametros,
                inputs=["Xt", "yt", "Xh", "yh"],
                outputs="metricas_hiperparametros",
                name="node_treino_otimiza_hiperparametros",
            )
        ]
    )


    return pipeline_split_data + pipeline_otimiza_hiperparametros
