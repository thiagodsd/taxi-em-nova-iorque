"""
This is a boilerplate pipeline 'transformacao'
generated using Kedro 0.17.6
"""

from typing import Any, Dict

import pandas as pd

def limpeza(data: pd.DataFrame) -> Dict[str, Any]:
    """limpeza"""
    return data