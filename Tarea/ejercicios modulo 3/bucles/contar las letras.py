cadena = "Hola"
contador = 0

for letra in cadena:
  if letra.isalpha():
    contador += 1

print("La cadena tiene", contador, "letras.")
