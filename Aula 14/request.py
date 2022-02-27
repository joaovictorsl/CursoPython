# Importando requests e o apelidando de req
import requests as req
# Utilizando método get do req para puxar dados de uma página web
res = req.get('https://api.github.com/users/torvalds')
# Transformando esses dados em um dicionário python
data = res.json()
print(data['name'])
print(data['company'])
print(type(data))
