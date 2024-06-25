from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RequestModel(BaseModel):
    batchid: str
    payload: List[List[int]]

class ResponseModel(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: Optional[datetime]
    completed_at: Optional[datetime]

