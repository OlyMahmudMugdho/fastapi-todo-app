from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

# DB Model
class Todo(Base):
    __tablename__ = 'todos'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String)
    body: str = Column(String)

    def __repr__(self) -> str:
        return "<User(id={self.id}, name={self.name}, age={self.age})>"
