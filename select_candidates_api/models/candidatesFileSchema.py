from pydantic import BaseModel

class CandidateFileIn(BaseModel):
    zip_path : str
    data_path : str
    extension : str
    performed_cleaning : str
    user_id : int

class CandidateFile(BaseModel):
    id : int
    zip_path : str
    data_path : str
    extension : str
    performed_cleaning : str
    user_id : int


class CandidateFileToDelete(BaseModel):
    user_pwd : str
    user_id : int
