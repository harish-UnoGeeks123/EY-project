from pydantic import BaseModel
from typing import List

class RequestModel(BaseModel):
    batchid: str
    payload: List[List[int]]