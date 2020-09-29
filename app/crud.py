from sqlalchemy.orm import Session

from . import models, schemas

#Gestion des Contactes des employés

def get_contacte_by_email(db: Session, email: str):
    '''Fonction permettant de réccupérer un contacte par 
    son email'''
    return db.query(models.Contacte).filter(models.Contacte.email == email).first()

def get_contacte_by_id(db: Session, id: int):
    '''Fonction permettant de réccupérer un contacte par 
    son ID'''
    return db.query(models.Contacte).filter(models.Contacte.id == id).first()

def get_contactes(db: Session, init: int = 0, limite: int = 100):
    '''Fonction permettant des reccupérer une liste des contactes 
    par rapport à leur ID. La liste étant limitée'''
    return db.query(models.Contacte).offset(init).limit(limite).all()

def create_contacte(db: Session, contacte: schemas.ContacteCreate):
    '''Cette fonction permet de créer des contactes'''
    db_contacte = models.Contacte(prenom=contacte.prenom, nom=contacte.nom,
     telephone=contacte.telephone, email=contacte.email,
     entreprise_id=contacte.entreprise_id)
    db.add(db_contacte)
    db.commit()
    db.refresh(db_contacte)
    return db_contacte

#Fin de la gestion des Contactes des employés


#Gestion des Entréprises

def get_entreprise_by_email(db: Session, email: str):
    '''Fonction permettant de réccupérer une entréprise par 
    son email'''
    return db.query(models.Entreprise).filter(models.Entreprise.email == email).first()

def get_entreprise_by_id(db: Session, id: int):
    '''Fonction permettant de réccupérer une entreprise par 
    son ID'''
    return db.query(models.Entreprise).filter(models.Entreprise.id == id).first()

def get_entreprises(db: Session, init: int = 0, limite: int = 100):
    '''Fonction permettant des reccupérer une liste des entréprises 
    par rapport à leur ID. La liste étant limitée'''
    return db.query(models.Entreprise).offset(init).limit(limite).all()

def create_entreprise(db: Session, entreprise: schemas.EntrepriseCreate):
    '''Cette fonction permet de créer des entréprises'''
    db_entreprise = models.Entreprise(nom=entreprise.nom, adresse=entreprise.adresse,
     telephone=entreprise.telephone, email=entreprise.email, 
     secteur_id=entreprise.secteur_id)
    db.add(db_entreprise)
    db.commit()
    db.refresh(db_entreprise)
    return db_entreprise

#Fin de la gestion des Entréprises



#Gestion des Secteurs

def get_secteur_by_nom(db: Session, nom: str):
    '''Fonction permettant de réccupérer un secteur par 
    son nom'''
    return db.query(models.Secteur).filter(models.Secteur.nom == nom).first()

def get_secteur_by_id(db: Session, id: int):
    '''Fonction permettant de réccupérer une secteur par 
    son ID'''
    return db.query(models.Secteur).filter(models.Secteur.id == id).first()

def get_secteurs(db: Session, init: int = 0, limite: int = 100):
    '''Fonction permettant des reccupérer une liste des secteurs 
    par rapport à leur ID. La liste étant limitée'''
    return db.query(models.Secteur).offset(init).limit(limite).all()

def create_secteur(db: Session, secteur: schemas.SecteurCreate):
    '''Cette fonction permet de créer des entréprises'''
    db_secteur = models.Secteur(nom=secteur.nom)
    db.add(db_secteur)
    db.commit()
    db.refresh(db_secteur)
    return db_secteur

#Fin de la gestion des Entréprises
