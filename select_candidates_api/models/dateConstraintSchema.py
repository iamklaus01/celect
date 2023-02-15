from typing import List
from pydantic import BaseModel
from tables import OptimizeType


class DateConstraintIn(BaseModel):
    min_date : str
    max_date : str
    optimize : OptimizeType
    feature_id : int

class DateConstraint(BaseModel):
    id : int
    min_date : str
    max_date : str
    optimize : OptimizeType
    feature_id : int


class AllDateConstraintIn(BaseModel):
    data : List[DateConstraintIn]
