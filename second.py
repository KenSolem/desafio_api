import requests

response = requests.get("https://reqres.in/api/users")
users_data = response.json()

# Extraer solo la lista de usuarios 
user_list = users_data['data']

# Imprime nombres y correos de los usuarios
for user in user_list:
  print(f"Nombre: {user['first_name']} {user['last_name']}, Correo: {user['email']}")
