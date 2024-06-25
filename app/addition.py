from fastapi import HTTPException
from app.models import ResponseModel
from datetime import datetime, timezone
from multiprocessing import Pool

def find_sum(numbers):
    return sum(numbers)

def perform_addition(request):
    numbers_list = request.payload

    if not all(isinstance(sublist, list) and all(isinstance(num, int) for num in sublist) for sublist in numbers_list):
        raise ValueError("All elements must be lists of integers")
    try:
        with Pool() as pool:
            result = pool.map(find_sum, numbers_list)
    except Exception as ex:
        return "Error: "+str(ex)

    return result

def add_numbers(request):
    try:
        started_at = datetime.now(timezone.utc)
        result = perform_addition(request)
        completed_at = datetime.now(timezone.utc)
        return ResponseModel(
            batchid=request.batchid,
            response=result,
            status="completed",
            started_at=started_at,
            completed_at=completed_at
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


