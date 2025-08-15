# Función que recibe dos tuplas y devuelve una nueva tupla
# con la suma de los elementos correspondientes
def sumar_tuplas(tupla1, tupla2):
    # Verificar que las tuplas tengan igual longitud
    if len(tupla1) != len(tupla2):
        print("Error: Las tuplas deben tener la misma longitud.")
        return ()

    # Lista para almacenar las sumas
    suma_elementos = []

    # Usamos un ciclo for para sumar elemento a elemento
    for i in range(len(tupla1)):
        suma = tupla1[i] + tupla2[i]
        suma_elementos.append(suma)

    # Convertimos la lista a tupla antes de devolver
    return tuple(suma_elementos)

# Tuplas de prueba
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Llamar a la función y mostrar el resultado
resultado = sumar_tuplas(t1, t2)
print("Suma de tuplas:", resultado)
