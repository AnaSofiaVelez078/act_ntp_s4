# Función que simula un sistema de votación con votos únicos usando conjunto
def sistema_votacion():
    votos = set()  # Conjunto para almacenar votos únicos (usuario-candidato)
    votos_candidatos = {}  # Diccionario para contar votos por candidato

    print("Sistema de votación. Escribe 'fin' para terminar.")

    while True:
        usuario = input("Nombre del votante: ").strip()
        if usuario.lower() == 'fin':
            break

        candidato = input("Nombre del candidato: ").strip()
        if candidato.lower() == 'fin':
            break

        # Crear un identificador único para voto (usuario, candidato)
        voto = (usuario.lower(), candidato.lower())

        if voto in votos:
            print(f"El usuario '{usuario}' ya votó por '{candidato}'. Voto duplicado no registrado.")
        else:
            votos.add(voto)
            # Contar voto para el candidato
            if candidato.lower() in votos_candidatos:
                votos_candidatos[candidato.lower()] += 1
            else:
                votos_candidatos[candidato.lower()] = 1
            print(f"Voto registrado: {usuario} -> {candidato}")

    # Mostrar resultados finales
    print("\nResultados de la votación:")
    if votos_candidatos:
        for candidato, cantidad in votos_candidatos.items():
            print(f"Candidato '{candidato}': {cantidad} voto(s)")
    else:
        print("No se registraron votos.")

# Ejecutar la función
sistema_votacion()
