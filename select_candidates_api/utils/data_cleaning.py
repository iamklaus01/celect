import numpy as np
import pandas as pd
import enum

from pandas.api.types import CategoricalDtype
from typing import List

class FeatureEngineeringType(enum.Enum):
    ADD = "add"
    SUBTRACT = "minus"
    DIVIDE = "divide"
    MULTIPLY = "times"
    CONCATENATE = "concatenate"

def remove_rows_with_only_missing_values(data: pd.DataFrame):
    new_data = data.dropna(how="all")
    return new_data


def remove_rows_with_percentage_of_missing_values(data: pd.DataFrame, percent:int):
    new_data = data[data.isnull().sum(axis=1) < percent]
    return new_data


def remove_cols_with_only_missing_values(data: pd.DataFrame):
    new_data = data.dropna(how="all", axis=1)
    return new_data


def remove_cols_with_percentage_of_missing_values(data: pd.DataFrame, percent:float):
    new_data = data[data.columns[data.isna().sum()/data.shape[0] < percent]]
    return new_data


def drop_columns(data:pd.DataFrame, cols : List[str]):
    new_data = data.drop(cols, axis=1)
    return new_data


def change_column_type(data:pd.DataFrame, col:str, type:str):
    data[col] = data[col].astype(type)
    return data

def change_col_to_datetime(data:pd.DataFrame, col:str):
    data[col] = pd.to_datetime(data[col])
    return data

def change_col_to_categorical_type(data:pd.DataFrame, col:str, list_of_ordered_values:List):
    if len(list_of_ordered_values) == 0:
        data[col] = data[col].astype("category")
    else:
        cat_dtype = CategoricalDtype(categories=list_of_ordered_values, ordered=True)
        data[col] = data[col].astype(cat_dtype)

    return data


def make_column_enum_values_uniform(data:pd.DataFrame, cols:List, right_value, list_of_wrong_values:List):
    for col in cols:
        data[col] = data[col].apply(lambda x: right_value if x in list_of_wrong_values else x)

    return data


def fill_missing_values_for_columns(data:pd.DataFrame, col:str, value):
    data[col].fillna(value, inplace = True)
    return data


def features_engineering(data:pd.DataFrame, new_col_name:str, col_1:str, col_2:str, operation_type:FeatureEngineeringType):

    if(operation_type == FeatureEngineeringType.ADD):
        data[new_col_name] = data[col_1] + data[col_2]
    elif(operation_type == FeatureEngineeringType.SUBTRACT):
        data[new_col_name] = data[col_1] - data[col_2]
    elif(operation_type == FeatureEngineeringType.MULTIPLY):
        data[new_col_name] = data[col_1] * data[col_2]
    elif(operation_type == FeatureEngineeringType.DIVIDE):
        data[new_col_name] = data[col_1] / data[col_2]
    elif(operation_type == FeatureEngineeringType.CONCATENATE):
        data[new_col_name] = data[col_1] + data[col_2]

    return data