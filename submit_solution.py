import requests

# Datos para el POST request
url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/devops"
data = {
    "name": "Simon Aguilera",
    "mail": "saguilera1608@gmail.com",  
    "github_url": "https://github.com/nomad3/devsecops-challenge.git"
}

# Realiza el POST request
response = requests.post(url, json=data)

# Verifica la respuesta
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
