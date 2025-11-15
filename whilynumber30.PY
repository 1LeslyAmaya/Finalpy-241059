numero = 1
suma = 0

while numero <= 30:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print(f"La suma de los números pares entre 1 y 30 es: {suma}")