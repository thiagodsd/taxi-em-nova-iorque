"""
This is a boilerplate pipeline 'treino'
generated using Kedro 0.17.6
"""

from typing import (
    Dict,
    #     List,
    #     Tuple,
    #     Set,
    #     Deque,
    #     NamedTuple,
    #     IO,
    #     Pattern,
    #     Match,
    #     Text,
    #     Optional,
    #     Sequence,
    #     Iterable,
    #     Mapping,
    #     MutableMapping,
        Any,
)


import numpy as np
import pandas as pd


from sklearn.impute          import SimpleImputer
from sklearn.compose         import ColumnTransformer
from sklearn.preprocessing   import OrdinalEncoder, OneHotEncoder, StandardScaler
from sklearn.pipeline        import Pipeline


def split_data(data: pd.DataFrame) -> Dict[str, Any]:
    r"""
    split_data
    """
    return dict(
        Xt=None,
        yt=None,
        Xh=None,
        yh=None
    )


def otimiza_hiperparametros(Xt: pd.DataFrame, yt: pd.DataFrame, Xh: pd.DataFrame, yh: pd.DataFrame) -> Dict[str, Any]:
    r"""
    otimiza_hiperparametros
    """
    return None