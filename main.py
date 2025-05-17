from fastapi import FastAPI
from controllers.todo_controller import router

# initialize the server
app = FastAPI()

# register the router
app.include_router(router=router, prefix="/todos", tags=["Todos"])
