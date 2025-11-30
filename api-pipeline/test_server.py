import requests

# Dirección ip
url1 = 'http://127.0.0.1:5000/ip'

response = requests.request("get", url1)

if response.status_code == 200:
    datos = response.json()
print(f'La dirección IP es {datos["ip"]}') # Mi driccion ip es

# MD5
texto = str(input('Dame el texto que quieras convertir en md5: '))

url2 = f'http://127.0.0.1:5000/md5/{texto}'

response = requests.request("get", url2)

if response.status_code == 200:
    datos = response.json()
print(f'El mensaje en md5 es: {datos["md5"]}')
