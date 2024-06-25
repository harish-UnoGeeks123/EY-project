# FastAPI Multiprocessing Example

This project demonstrates a FastAPI application that performs addition on lists of integers using Python's multiprocessing pool. The project is organized following the MVC (Model-View-Controller) pattern.

## Project Structure

fastapi_project/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── controllers.py     # Contains endpoints
│ ├── models.py          # Contains Request and Response classes
│ ├── addition.py        # Since there is no html rendering involved here, views.py is not developed.
│ ├── error_handler.py   # For error handling
│ ├── logger.py          # for logging
│ ├── tests/             
│ │ ├── init.py
│ │ ├── test_addition.py
├── requirements.txt
└── README.md


## Requirements(latest version)

- Python 3.8+
- fastapi
- uvicorn
- pytest

## Installation

1. **Clone the repository**:
    ```sh
    git clone 
    cd EY project           # This is the root folder for the project
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

Start the FastAPI application using Uvicorn:
```sh
uvicorn app.main:app --reload

## Testing the code
pytest .\app\tests\


## Testing the APIs using POSTMAN or fastapi swagger UI (http://127.0.0.1:8000/docs)

# Sample input:
method: POST
endpoint: http://127.0.0.1:8000/api/add/
Request body:
            {
                "batchid": "id0101",
                "payload": [[1, 2], [3, 4]]
            }

# Expected output:
            {
                "batchid": "id0101",
                "response": [3, 7],
                "status": "complete",
                "started_at": "2024-06-25T12:34:56.789123",
                "completed_at": "2024-06-25T12:34:56.890123",
            }
