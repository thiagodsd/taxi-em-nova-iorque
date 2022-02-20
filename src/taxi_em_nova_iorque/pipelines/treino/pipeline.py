"""
This is a boilerplate pipeline 'treino'
generated using Kedro 0.17.6
"""

from xml.etree.ElementTree import PI
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import (
    separa_conjuntos,
    selecao_features,
    hiperparametros,
    selecao_modelos,
    treinamento_modelo,
    kfold_cross_validation,
    avaliacao_modelo
    )


def create_pipeline(**kwargs) -> Pipeline:
    separa_conjuntos_pipeline = Pipeline(
        [
            node(
                separa_conjuntos, 
                inputs = "treino_features",
                outputs = ['Xt', 'yt', 'Xh', 'yh']
            ),
        ]
    )

    seleciona_variaveis_pipeline = Pipeline(
        [
            node(
                selecao_features, 
                inputs = ['Xt', 'yt'],
                outputs = None
            ),
        ]
    )

    return separa_conjuntos_pipeline + seleciona_variaveis_pipeline