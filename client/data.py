import requests

# URL da API
url = "https://fakestoreapi.com/products"
categoria = url + "/categories"
eletronico = url + "/category/electronics"
jewelery = url + "/category/jewelery"

# Fazendo a solicitação GET para obter os produtos
pdt_response = requests.get(url)
categoria_response = requests.get(categoria)
eletronico_response = requests.get(eletronico)
jewelery_response = requests.get(jewelery)

# transforma a request em uma lista
products = pdt_response.json()
categorias = categoria_response.json()
eletronicos = eletronico_response.json()
jeweleries = jewelery_response.json()
