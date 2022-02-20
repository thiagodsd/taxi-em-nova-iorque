"""
This is a boilerplate pipeline 'treino'
generated using Kedro 0.17.6
"""

from typing import (
    Dict,
    List,
    Tuple,
    Set,
    Deque,
    NamedTuple,
    IO,
    Pattern,
    Match,
    Text,
    Optional,
    Sequence,
    Iterable,
    Mapping,
    MutableMapping,
    Any,
)

import pandas as pd


def separa_conjuntos(data: pd.DataFrame) -> pd.DataFrame:
    """separa_conjuntos"""
    return Xt, yt, Xh, yh


def selecao_features(X: pd.DataFrame, y: pd.DataFrame) -> Dict:
    """selecao_features"""
    d = dict()
    return d


def hiperparametros(Xt: pd.DataFrame, yt: pd.DataFrame) -> Dict:
    """hiperparametros"""
    d = dict()
    return d


def selecao_modelos(data: pd.DataFrame) -> pd.DataFrame:
    """selecao_modelos"""
    return data


def treinamento_modelo(data: pd.DataFrame) -> pd.DataFrame:
    """treinamento_modelo"""
    return data


def kfold_cross_validation(data: pd.DataFrame) -> Dict:
    """kfold_cross_validation"""
    return data


def avaliacao_modelo(data: pd.DataFrame) -> Dict:
    """avaliacao_modelo"""
    return data