import requests
import json

url = 'https://serverest.dev/'

nome = "Anne Vitoria"
email = "annev@gmail.com"
passw = "teste"

# Criar usuario administrador

create = {
    "nome": nome,
    "email": email,
    "password": passw,
    "administrador": "true"
}

res = requests.post(url+"usuarios", data=create)
dat = json.loads(res.text)
print(res.text)

# getUsuario

idUsuario = dat["_id"]
res = requests.get(url+"usuarios?_id="+idUsuario)
print(res.text)

# Login

login = {
    "email": email,
    "password": passw
}

res = requests.post(url+"login", data=login)
dat = json.loads(res.text)
print(res.text)


# Cadastro Produto

token = dat["authorization"]

nomep = "Kindle 3.0"
preco = "800"
descricao = "Otimo para leitura"
qtd = "20"

produto = {
    "nome": nomep,
    "preco": preco,
    "descricao": descricao,
    "quantidade": qtd
}

headers = {"authorization": token}

res = requests.post(url+'produtos', data=produto, headers=headers)
dat = json.loads(res.text)
print(res.text)


# Get Produto
idProduto = dat["_id"]
res = requests.get(url+"produtos?_id="+idProduto)
print(res.text)
