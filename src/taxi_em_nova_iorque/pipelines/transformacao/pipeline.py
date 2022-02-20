"""
This is a boilerplate pipeline 'transformacao'
generated using Kedro 0.17.6
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import limpeza, novas_features_simples, novas_features_complexas, concatena


def create_pipeline(**kwargs) -> Pipeline:
    pipeline_limpeza = Pipeline(
        [
            node(
                limpeza,
                inputs="treino",
                outputs="tabela_limpa",
                name="node_treino_limpeza",
            )
        ]
    )

    pipeline_novas_features = Pipeline(
        [
            node(
                limpeza,
                inputs="treino",
                outputs="tabela_limpa",
                name="node_treino_limpeza",
            ),
            node(
                novas_features_simples,
                inputs="tabela_limpa",
                outputs="tabela_feature_simples",
                name="node_treino_novas_features_simples",
            ),
            node(
                novas_features_complexas,
                inputs=["tabela_limpa", "params:complex_treino", "params:complex_frac"],
                outputs=dict(
                    features_complexas="tabela_feature_complexa",
                    modelo_dbscan="modelo_dbscan",
                    modelo_kmeans="modelo_kmeans",
                ),
                name="node_treino_novas_features_complexas",
            ),
            node(
                concatena,
                inputs=[
                    "tabela_limpa",
                    "tabela_feature_simples",
                    "tabela_feature_complexa",
                ],
                outputs="treino_features",
                name="node_treino_concatena",
            ),
        ]
    )

    return pipeline_limpeza + pipeline_novas_features
