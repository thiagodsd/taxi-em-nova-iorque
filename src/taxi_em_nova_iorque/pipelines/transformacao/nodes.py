"""
This is a boilerplate pipeline 'transformacao'
generated using Kedro 0.17.6
"""

from typing import (
    Dict
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
#     Any,
)

from math import (
    sin,
    cos,
    sqrt,
    atan2, 
    radians
)

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN


def lat_lon_converter(lat1, lon1, lat2, lon2, unit):
    """
    ref: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    """
    try:
        R = 6373.0
        dlon = radians(lon2) - radians(lon1)
        dlat = radians(lat2) - radians(lat1)
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        if unit == 'm':
            return distance * 10e3
        elif unit == 'km':
            return distance
    except ValueError:
        return np.nan


def dbscan_predict(model, X):
    """
    ref: https://stackoverflow.com/questions/27822752/scikit-learn-predicting-new-points-with-dbscan
    """
    nr_samples = X.shape[0]

    y_new = np.ones(shape=nr_samples, dtype=int) * -1

    for i in range(nr_samples):
        diff = model.components_ - X[i, :]   # NumPy broadcasting
        dist = np.linalg.norm(diff, axis=1)  # Euclidean distance
        shortest_dist_idx = np.argmin(dist)

        if dist[shortest_dist_idx] < model.eps:
            y_new[i] = model.labels_[model.core_sample_indices_[shortest_dist_idx]]

    return y_new


def limpeza(data: pd.DataFrame) -> pd.DataFrame:
    """limpeza"""
    return data.drop(columns=["id"])


def novas_features_simples(data: pd.DataFrame) -> pd.DataFrame:
    """
    novas_features_simples
    """
    # features temporais
    data['pickup_dt'] = pd.to_datetime(data['pickup_datetime'], format='%Y-%m-%d %H:%M:%S', errors='ignore')
    data = data.drop(columns=['pickup_datetime'])

    data['pick_minute'] = data['pickup_dt'].dt.minute
    data['pick_hour'] = data['pickup_dt'].dt.hour
    data['pick_day'] = data['pickup_dt'].dt.day
    data['pick_month'] = data['pickup_dt'].dt.month
    data['pick_year'] = data['pickup_dt'].dt.year
    data['pick_quarter'] = data['pickup_dt'].dt.quarter
    data['pick_weekofyear'] = data['pickup_dt'].dt.weekofyear

    # features espaciais
    data['lon_lat_manhattan'] = abs(data['dropoff_longitude']-data['pickup_longitude']) + abs(data['dropoff_latitude']-data['pickup_latitude'])
    data['dist_manhattan_meter'] = data.apply( lambda x: lat_lon_converter(
        x['pickup_latitude'], x['pickup_longitude'], 
        x['dropoff_latitude'], x['dropoff_longitude'], 'm'), axis=1 )
    
    novas_features = ['pickup_dt', 'pick_minute', 'pick_hour', 'pick_day', 
                      'pick_month', 'pick_year', 'pick_quarter', 'pick_weekofyear',
                      'lon_lat_manhattan', 'dist_manhattan_meter']
    
    return data[novas_features]


def novas_features_complexas(data: pd.DataFrame, fit_obs: bool) -> Dict:
    """
    novas_features_complexas
    """
    coordenadas = ['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']
    data_sample = data[coordenadas].sample(frac=0.5, random_state=22)
    X = StandardScaler().fit_transform(data_sample.values)

    if fit_obs == True:
        db = DBSCAN(eps=0.75, min_samples=10).fit(X)
        kmeans = KMeans(n_clusters=5, random_state=37).fit(X)

        data['db_predict'] = dbscan_predict(db, StandardScaler().fit_transform(data[coordenadas].values))
        data['kmeans_predict'] = kmeans.predict(StandardScaler().fit_transform(data[coordenadas].values))
        return dict(
            features_complexas = data,
            modelo_dbscan = db,
            modelo_kmeans = kmeans
        )
    else:
        return data


def concatena(data_limpo: pd.DataFrame, data_simples: pd.DataFrame, data_complex: pd.DataFrame) -> pd.DataFrame:
    """
    novas_features_complexas
    """
    return pd.concat([data_limpo, data_simples, data_complex], axis=1)
