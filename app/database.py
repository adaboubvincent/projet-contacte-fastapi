'''Fichier permettant de relier notre aplication à une base 
de données'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/fastapi"
SQLALCHEMY_DATABASE_URL ="postgres://hmzfwjaablpcld:ad0854bd76281509931756b9bf31bc196b971c7259e8acf99190d7779f7c4d9d@ec2-34-238-26-109.compute-1.amazonaws.com:5432/db92ma3odp73g6"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()