# Todo App
This is a simple Todo REST API

## Tech Stack
- Python 3.12.3
- Fast API
- SQLAlchemy
- PostgreSQL

## Prerequisites
- PostgreSQL
- Python 3

# How to run
1. First clone the repo
    ```bash
    https://github.com/OlyMahmudMugdho/fastapi-todo-app
    ```

2. Create a virtual environment
    ```bash
    python -m venv .venv && source .venv/bin/activate
    ```

3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Run the server
   Modify the DB_URI from the .env file according to you and run:
    ```bash
    uvicorn main:app --reload
    ```