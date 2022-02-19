"""
This is a boilerplate pipeline 'transformacao'
generated using Kedro 0.17.6
"""

from typing import Any, Dict

import pandas as pd


def limpeza(data: pd.DataFrame) -> pd.DataFrame:
    """limpeza"""
    return data


def novas_features_simples(data: pd.DataFrame) -> pd.DataFrame:
    """novas_features_simples"""
    return data


def novas_features_complexas(data: pd.DataFrame) -> pd.DataFrame:
    """novas_features_complexas"""
    return data

def concatena(data_simples: pd.DataFrame, data_complex: pd.DataFrame) -> pd.DataFrame:
    """novas_features_complexas"""
    return None