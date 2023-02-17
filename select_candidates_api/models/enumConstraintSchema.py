from typing import List
from pydantic import BaseModel

from db.tables import Metric, OptimizeType


class EnumConstraintIn(BaseModel):
    value : str
    number : int
    metric : Metric
    feature_id : int
    weight : int
    optimize : OptimizeType

class EnumConstraint(BaseModel):
    id : int
    value : str
    number : int
    metric : Metric
    feature_id : int
    weight : int
    optimize : OptimizeType


class AllEnumConstraintIn(BaseModel):
    data : List[EnumConstraintIn]
