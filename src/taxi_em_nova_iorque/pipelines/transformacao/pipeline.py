"""
This is a boilerplate pipeline 'transformacao'
generated using Kedro 0.17.6
"""

from xml.etree.ElementTree import PI
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import limpeza, novas_features_simples, novas_features_complexas, concatena


def create_pipeline(**kwargs) -> Pipeline:
    template_treino = Pipeline(
        [
            node(
                limpeza, 
                inputs = "treino",
                outputs = "tabela_limpa"
            ),
            node(
                novas_features_simples, 
                inputs = "tabela_limpa",
                outputs = "tabela_feature_simples"
            ),
            node(
                novas_features_complexas, 
                inputs = "tabela_limpa",
                outputs = "tabela_feature_complexa"
            ),
            node(
                concatena, 
                inputs = ["tabela_feature_simples", "tabela_feature_complexa"],
                outputs = "treino_features"
            ),
        ]
    )

    template_teste = Pipeline(
        [
            node(
                limpeza, 
                inputs = "teste",
                outputs = "tabela_limpa"
            ),
            node(
                novas_features_simples, 
                inputs = "tabela_limpa",
                outputs = "tabela_feature_simples"
            ),
            node(
                novas_features_complexas, 
                inputs = "tabela_limpa",
                outputs = "tabela_feature_complexa"
            ),
            node(
                concatena, 
                inputs = ["tabela_feature_simples", "tabela_feature_complexa"],
                outputs = "teste_features"
            ),
        ]
    )

    treino_pipeline = pipeline(
        pipe = template_treino,
        inputs="treino",
        namespace="trata_treino"
    )

    teste_pipeline = pipeline(
        pipe = template_teste,
        inputs="teste",
        namespace="trata_teste"
    )


    pipeline_final = pipeline(
        pipe = treino_pipeline + teste_pipeline,
        namespace="prepara_dados"
    )    

    return pipeline_final