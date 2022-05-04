"""Module to generate random users"""
from faker import Faker
from pprint import pprint
import logging
from pathlib import Path

#Utilisation de la class Path pour générer le chemin vers le fichier user.py
#la méthode resolve nous permet de nous affranchir de tout chemin relatif
#parent nous permet de remonter au dossier parent ici USERGENERATOR
BASE_DIR = Path(__file__).resolve().parent

#Création du chemin vers le fichier user.log dans lequel
#seront reportés les erreurs d
logging.basicConfig(
    filename=BASE_DIR / "user.log", 
    level=logging.WARNING, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode="w")

fake = Faker()

def getUser():
    """Generate a single user
    Returns:
        str: user
    """
    return f"{fake.first_name()} {fake.last_name()}"

def getUsers(n: int)->list:
    """Generate a list of users
    Args:
        n (int): number of users
    Returns:
        list[str]: users
    """
    return [getUser() for _ in range(n)]

if __name__ == "__main__":
    # user = getUser()
    # pprint(user)
    users = getUsers(5)
    pprint(users)
