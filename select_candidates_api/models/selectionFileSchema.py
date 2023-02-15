from pydantic import BaseModel


class SelectionFileIn(BaseModel):
    encoded_file : str
    status : str
    nb_sol : int
    satisfaction : int
    features : str
    candidatesFile_id : int

class SelectionFile(BaseModel):
    id : int
    encoded_file : str
    status : str
    nb_sol : int
    satisfaction : int
    features: str
    candidatesFile_id : int

class SelectionFileToDelete(BaseModel):
    user_pwd : str
    user_id : int