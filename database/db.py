import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.todo import Base

# setup database
engine = create_engine(os.getenv("DB_URI"))

# create the session
Session = sessionmaker(bind=engine)
session = Session()

# create the table(s)
Base.metadata.create_all(engine)