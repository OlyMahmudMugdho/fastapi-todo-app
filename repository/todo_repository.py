from model.todo import Todo
from sqlalchemy.orm import Session

# Repository to perform database related operations
class TodoRepository:

    # contructor, session injected as a dependency
    def __init__(self, session: Session):
        self.session: Session = session

    # create todo operation
    def create_todo(self, todo: Todo) -> Todo | None:
        try:
            self.session.add(todo)
            self.session.commit()
            return todo
        except Exception as exception:
            print(exception)
            return None

    # get todo by id
    def get_todo_by_id(self, id: int) -> Todo | None:
        return self.session.query(Todo).filter_by(id=id).first()
    
    
