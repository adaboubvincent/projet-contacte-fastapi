'''Ce fichier nous permet de mettre en place le schema que suit 
le models de notre application'''
from typing import List, Optional

from pydantic import BaseModel

#Mise en place le schema de la tableau contacte
class ContacteBase(BaseModel):
    prenom: str
    nom: Optional[str] = None
    email: Optional[str] = None
    telephone: Optional[str] = None
    entreprise_id: Optional[int] = None

class ContacteCreate(ContacteBase):
    pass

class Contacte(ContacteBase):
    id: int

    class Config:
        orm_mode = True
#Fin de mise en place du schema de la table contacte


#Mise en place le schema de la tableau entreprise
class EntrepriseBase(BaseModel):
    nom: str
    adresse: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    secteur_id: Optional[int] = None
    

class EntrepriseCreate(EntrepriseBase):
    pass

class Entreprise(EntrepriseBase):
    id: int
    #employees: List[Contacte] = []
    
    class Config:
        orm_mode = True
#Fin de mise en place du schema de la table entreprise


#Mise en place le schema de la tableau secteur
class SecteurBase(BaseModel):
    nom: str

class SecteurCreate(SecteurBase):
    pass

class Secteur(SecteurBase):
    id: int
    #entreprises: List[Entreprise] = []
    
    class Config:
        orm_mode = True
#Fin de mise en place du schema de la table secteur



#Mise en place le schema de la tableau token, user et tokenData
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    hashed_password: Optional[str] = None
    disabled: Optional[bool] = None
    

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str
#Fin de mise en place du schema de la tableau token, user et tokenData