"""
This is a boilerplate pipeline 'transformacao'
generated using Kedro 0.17.6
"""

from kedro.pipeline import Pipeline, node

from .nodes import limpeza

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            limpeza, 
            inputs = ["treino"],
            outputs = ["treino_limpo"]
        ),
        node(
            limpeza, 
            inputs = ["teste"],
            outputs = ["teste_limpo"]
        )
    ])
