from fastapi import APIRouter
from app.models.resquest import RequestModel
from app.models.response import ResponseModel
from app.views.addition import add_numbers

router = APIRouter()

@router.post("/add", response_model=ResponseModel)
def add_list_of_numbers(request: RequestModel):
    return add_numbers(request)

@router.get("/")
def root():
    return "This is home page."