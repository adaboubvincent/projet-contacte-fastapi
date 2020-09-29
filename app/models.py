'''Le fichier permettant de mettre en place le models de notre 
base de données'''

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

#L'entité Secteur
class Secteur(Base):
    '''Elle nous permet de créer des secteurs'''

    __tablename__ = "secteurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=True)

    entreprises = relationship("Entreprise", back_populates="secteur")

#L'entité Entreprise
class Entreprise(Base):
    '''Elle nous permettra de créer des entréprises qui seront dans
    un secteur donné'''

    __tablename__ = "entreprises"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=True)
    adresse = Column(String(100))
    telephone = Column(String(20), unique=True)
    email = Column(String(100), unique=True)

    secteur_id = Column(Integer, ForeignKey("secteurs.id"))
    secteur = relationship("Secteur", back_populates="entreprises")

    employees = relationship("Contacte", back_populates="entreprise")

#L'entité Contacte
class Contacte(Base):
    '''Elle nous permettra de créer des contactes des utilisateurs 
    qui sont dans un secteur donné'''

    __tablename__ = "contactes"

    id = Column(Integer, primary_key=True, index=True)
    prenom = Column(String(100))
    nom = Column(String(100))
    email = Column(String(100), index=True, unique=True)
    telephone = Column(String(20), unique=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id"))


    entreprise = relationship("Entreprise", back_populates="employees")



#L'entité User
class User(Base):
    '''Elle nous permettra de créer des utilisateurs '''

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    full_name = Column(String(100))
    hashed_password = Column(String(200))
    email = Column(String(100), index=True, unique=True)
    disabled = Column(Boolean, default=False)



#L'entité Token
class Token(Base):
    '''Elle nous permettra de créer des utilisateurs '''

    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String(100))
    token_type = Column(String(100))