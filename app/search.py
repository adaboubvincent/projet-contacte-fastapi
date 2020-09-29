'''Dans ce fichier, nous alloons mettre en place une méthode permettant de faire des recherche'''

from sqlalchemy.orm import Session
from . import models, schemas

def get_resultats(db: Session, q: str = None):

    contactes: object =  db.query(models.Contacte).all() #Réccupération de tous les contactes
    entreprises: object =  db.query(models.Entreprise).all() #Réccupération de toutes les entréprises
    secteurs: object =  db.query(models.Secteur).all() #Réccupération de tous les secteurs

    listeContactes = [] #Initialisatiion de la liste pour les contactes
    listeEntreprises = [] #Initialisatiion de la liste pour les entréprises
    listeSecteurs = [] #Initialisatiion de la liste pour les secteurs

    q = q.upper()

    for contacte in list(contactes) :
    	if contacte.nom.upper().find(q) != -1 or contacte.prenom.upper().find(q) != -1 or contacte.email.upper().find(q) != -1 or contacte.telephone.upper().find(q) != -1:
    		listeContactes.append(contacte)
    for entreprise in list(entreprises):
      if entreprise.nom.upper().find(q) != -1 or entreprise.email.upper().find(q) != -1 or entreprise.adresse.upper().find(q) != -1 or contacte.telephone.upper().find(q) != -1:
        listeEntreprises.append(entreprise)


    for secteur in list(secteurs):
      if secteur.nom.upper().find(q) != -1 :
        listeSecteurs.append(secteur)

    dictSEC = {} #Initialisation du dictionnaire qui contiendra les contactes, entréprises et secteurs

    #Ajout des résultats dans le dictiionnaire
    dictSEC['secteurs'] = listeSecteurs
    dictSEC['entreprises'] = listeEntreprises
    dictSEC['employees'] = listeContactes


    return {'resultats' : dictSEC}