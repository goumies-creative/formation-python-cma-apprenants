# Faire une démo pip install requests en live
import requests

response = requests.get("https://api.github.com")
print(f"Statut de la requête vers GitHub API : {response.status_code}") 

response_cours = requests.get("https://github.com/goumies-creative/formation-python-cma-apprenants")
print(f"Contenu projet support cours Python SCAP : {response_cours.content}") 
