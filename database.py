from sqlalchemy import create_engine
from sqlalchemy import sessionmaker


SQL_URL=""

engine = create_engine(SQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=Fasle, bind=engine) #to create session objects
