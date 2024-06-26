# FastAPI Multiprocessing Example

This project demonstrates a FastAPI application that performs addition on lists of integers using Python's multiprocessing pool. The project is organized following the MVC (Model-View-Controller) pattern.

## Project Structure

my_fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── request.py
│   │   ├── response.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── addition.py       # return list addition ouput
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── controllers.py     # Contains endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── error_handler.py
│   │   ├── logger.py
│   └── tests/
│       ├── __init__.py
│       ├── test_app.py          
├── .env
├── requirements.txt
└── README.md

## Requirements(latest version)

- Python 3.12.2 # The code works on latest python version
- fastapi
- uvicorn
- pytest

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/harish-UnoGeeks123/EY-project.git
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
