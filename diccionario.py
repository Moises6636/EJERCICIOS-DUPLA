# Crea un diccionario llamado contactos con al menos tres amigos
contactos = {
    "Amigo1": "1234567890",
    "Amigo2": "9876543210",
    "Amigo3": "4567890123"
}

# Imprime el número de teléfono de uno de tus amigos buscando en el diccionario por su nombre
nombre_amigo = "Amigo1"
numero_telefono = contactos[nombre_amigo]
print(f"El número de teléfono de {nombre_amigo} es: {numero_telefono}")

# Actualiza el número de teléfono de uno de tus amigos en el diccionario
nuevo_numero = "5555555555"
contactos["Amigo1"] = nuevo_numero

# Imprime el diccionario actualizado
print("Diccionario actualizado:")
print(contactos)
