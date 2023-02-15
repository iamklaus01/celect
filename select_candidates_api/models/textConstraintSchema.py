from typing import List
from pydantic import BaseModel
from tables import OptimizeType


class TextConstraintIn(BaseModel):
    must_contain : str
    weight : int
    optimize : OptimizeType
    feature_id : int

class TextConstraint(BaseModel):
    id : int
    must_contain : str
    weight : int
    optimize : OptimizeType
    feature_id : int


class AllTextConstraintIn(BaseModel):
    data : List[TextConstraintIn]
