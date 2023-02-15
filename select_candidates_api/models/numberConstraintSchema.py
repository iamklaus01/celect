from typing import List
from pydantic import BaseModel

from tables import OptimizeType


class IntegerConstraintIn(BaseModel):
    min_value : float
    max_value : float
    mean_value : float
    coefficient : float
    optimize : OptimizeType
    feature_id : int

class IntegerConstraint(BaseModel):
    id : int
    min_value : float
    max_value : float
    mean_value : float
    coefficient : float
    optimize : OptimizeType
    feature_id : int


class AllIntegerConstraintIn(BaseModel):
    data : List[IntegerConstraintIn]