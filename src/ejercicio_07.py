# Función que recibe una tupla de estudiantes (nombre, edad, promedio)
# y devuelve una nueva tupla solo con los estudiantes cuyo promedio es mayor a 8.0
def estudiantes_aprobados(estudiantes):
    # Lista para almacenar estudiantes con promedio > 8.0
    aprobados = []

    # Recorrer cada estudiante en la tupla
    for estudiante in estudiantes:
        nombre, edad, promedio = estudiante  # Desempaquetar la tupla

        # Verificar si el promedio es mayor a 8.0
        if promedio > 8.0:
            aprobados.append(estudiante)  # Agregar a la lista de aprobados

    # Convertir la lista a tupla antes de devolverla
    return tuple(aprobados)

# Tupla de prueba con estudiantes (nombre, edad, promedio)
estudiantes = (
    ("Ana", 20, 8.5),
    ("Luis", 22, 7.9),
    ("Marta", 19, 9.1),
    ("Jorge", 21, 6.8),
    ("Sofía", 20, 8.2)
)

# Llamar a la función y mostrar resultado
aprobados = estudiantes_aprobados(estudiantes)
print("Estudiantes con promedio mayor a 8.0:")
for estudiante in aprobados:
    print(estudiante)
