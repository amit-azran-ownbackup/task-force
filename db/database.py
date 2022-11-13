from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "postgresql://admin:1234@localhost/ob_db_fetcher_server"

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

