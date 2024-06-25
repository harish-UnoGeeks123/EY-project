from fastapi import APIRouter
from app.models import RequestModel, ResponseModel
from app.addition import add_numbers

router = APIRouter()

@router.post("/add", response_model=ResponseModel)
def add_list_of_numbers(request: RequestModel):
    return add_numbers(request)
