from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, crud, search, authentificated
from app.database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get():
    '''Méthode d'accueil '''
    
    return {'message' : 'Well come my friend to my fastapi project'}

@app.post("/secteur/ajouter/")
def create_secteur(secteur: schemas.SecteurCreate, db: Session = Depends(get_db)):
    '''Méthode permettant d'ajouter un secteur'''
    db_secteur = crud.get_secteur_by_nom(db, nom=secteur.nom)
    if db_secteur:
        raise HTTPException(status_code=400, detail="Secteur déjà enrégistré avec cet nom")
    return crud.create_secteur(db=db, secteur=secteur)

@app.get("/secteurs/", response_model=List[schemas.Secteur])
def read_secteurs(init: int = 0, limite: int = 100, db: Session = Depends(get_db)):
    '''Méthode permettant de liste des secteurs des entréprises
    selon l'intervalle donné'''
    secteurs = crud.get_secteurs(db, init=init, limite=limite)
    return secteurs

@app.get("/secteur/{id}")
def read_secteur(id: int, db: Session = Depends(get_db)):
    '''Méthode permettant de rechercher un secteur à partir de son Id'''
    secteur = crud.get_secteur_by_id(db, id)
    return secteur



@app.post("/entreprise/ajouter/")
def create_secteur(entreprise: schemas.EntrepriseCreate, db: Session = Depends(get_db)):
    '''Méthode permettant d'ajouter une entreprise'''
    db_entreprise = crud.get_entreprise_by_email(db, email=entreprise.email)
    if db_entreprise:
        raise HTTPException(status_code=400, detail="Entreprise déjà enrégistrée avec cet nom")
    return crud.create_entreprise(db=db, entreprise=entreprise)

@app.get("/entreprises/", response_model=List[schemas.Entreprise])
def read_entreprises(init: int = 0, limite: int = 100, db: Session = Depends(get_db)):
    '''Méthode permettant de liste des entreprises
    selon l'intervalle donné'''
    entreprises = crud.get_entreprises(db, init=init, limite=limite)
    return entreprises

@app.get("/entreprise/{id}")
def read_secteur(id: int, db: Session = Depends(get_db)):
    '''Méthode permettant de rechercher une entreprise à partir de son Id'''
    entreprise = crud.get_entreprise_by_id(db, id)
    return entreprise


@app.post("/contacte/ajouter/")
def create_contacte(contacte: schemas.ContacteCreate, db: Session = Depends(get_db)):
    '''Méthode permettant d'ajouter un contacte'''
    db_contacte = crud.get_contacte_by_email(db, email=contacte.email)
    if db_contacte:
        raise HTTPException(status_code=400, detail="Contacte déjà enrégistré avec cet nom")
    return crud.create_contacte(db=db, contacte=contacte)

@app.get("/contactes/", response_model=List[schemas.Contacte])
def read_contactes(init: int = 0, limite: int = 100, db: Session = Depends(get_db)):
    '''Méthode permettant de liste des contactes
    selon l'intervalle donné'''
    contactes = crud.get_contactes(db, init=init, limite=limite)
    return contactes

@app.get("/contacte/{id}")
def read_contacte(id: int, db: Session = Depends(get_db)):
    '''Méthode permettant de rechercher un contacte à partir de son Id'''
    contacte = crud.get_contacte_by_id(db, id)
    return contacte


@app.get("/rechercher/{q}")
def read_root(db: Session = Depends(get_db), q: str = None):
    return search.get_resultats(db, q)


#Gestion d'utilisateur
@app.post("/utilisateur/creer/")
def create_contacte(user: schemas.UserCreate, db: Session = Depends(get_db)):
    '''Méthode permettant d'ajouter un contacte'''
    db_user = authentificated.get_user(db, username=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User déjà enrégistré avec cet nom")
    return authentificated.create_user(db=db, user=user)

#Gestion des authentification par le token
# @app.post("/token", response_model=schemas.Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(get_db)):
#     user = authentificated.authenticate_user(Depends(get_db).query(models.User).all(), form_data.username, form_data.password)

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=authentificated.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = authentificated.create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    user = authentificated.authenticate_user(db, form_data.username, form_data.password)
    print(users)
    print(user)
    print(form_data.username)
    print(form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(authentificated.get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: schemas.User = Depends(authentificated.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
