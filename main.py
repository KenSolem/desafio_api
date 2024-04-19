import requests

# 1. Obtener información de usuarios
response = requests.get("https://reqres.in/api/users")
users_data = response.json()
print(users_data)

# 2. Crear un usuario
new_user = {
    "name": "Ignacio",
    "job": "Profesor"
}
response = requests.post("https://reqres.in/api/users", json=new_user)
created_user = response.json()
print(created_user)

# 3. Actualizar un usuario
updated_user_data = {
    "residence": "zion"
}
response = requests.put(f"https://reqres.in/api/users/morpheus", json=updated_user_data)
updated_user = response.json()
print(updated_user)

# 4. Eliminar un usuario
response = requests.delete(f"https://reqres.in/api/users/Tracey")
print(response.status_code)
