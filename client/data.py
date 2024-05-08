import requests

# URL da API
url = "https://fakestoreapi.com/products"
categoria = url + "/categories"
eletronico = url + "/category/electronics"
jewelery = url + "/category/jewelery"
men_clothing = url + "/category/men's%20clothing"
women_clothing = url + "/category/women's%20clothing"

# Fazendo a solicitação GET para obter os produtos
pdt_response = requests.get(url)
categoria_response = requests.get(categoria)
eletronico_response = requests.get(eletronico)
jewelery_response = requests.get(jewelery)
men_clothing_response = requests.get(men_clothing)
women_clothing_response = requests.get(women_clothing)

# transforma a request em uma lista
products = pdt_response.json()
categorias = categoria_response.json()
eletronicos = eletronico_response.json()
jeweleries = jewelery_response.json()
men_clothing = men_clothing_response.json()
women_clothing = women_clothing_response.json()
