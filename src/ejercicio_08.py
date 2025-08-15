# Función que genera una tupla con los primeros 20 números de Fibonacci
# y luego muestra solo los números impares
def fibonacci_impares():
    # Lista para almacenar la secuencia
    fibonacci = []

    # Inicializamos los primeros dos números de Fibonacci
    a, b = 0, 1

    # Usamos un ciclo while para generar los primeros 20 números
    while len(fibonacci) < 20:
        fibonacci.append(a)
        a, b = b, a + b  # Actualizamos los valores para la siguiente iteración

    # Convertimos la lista a tupla (inmutable)
    fibonacci_tupla = tuple(fibonacci)

    # Mostrar todos los números impares usando un ciclo for
    print("Números impares en la secuencia de Fibonacci:")
    for num in fibonacci_tupla:
        if num % 2 != 0:  # Verificar si es impar
            print(num)

    # Devolver la tupla con la secuencia completa
    return fibonacci_tupla

# Llamamos a la función y almacenamos la tupla
fib_tupla = fibonacci_impares()
