import requests


def consultar_pokemon_avanzado():
    print("¡Consulta Pokémon con manejo avanzado de errores!")

    nombre_pokemon = input("Ingresa el nombre de un Pokémon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    try:
        respuesta = requests.get(url)

        if respuesta.status_code == 404:
            print(f"Error: El Pokémon '{nombre_pokemon}' no existe (Error 404).")
            return

        if respuesta.status_code != 200:
            print(f"Error: Respuesta inesperada del servidor (código {respuesta.status_code}).")
            return

        datos = respuesta.json()
        if not datos:
            print("Error: La respuesta de la API está vacía.")
            return

        print(f"Pokémon '{nombre_pokemon.capitalize()}' encontrado:")
        print(f"  - Altura: {datos['height']}")
        print(f"  - Peso: {datos['weight']}")

    except requests.ConnectionError:
        print("Error: No hay conexión a Internet.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    consultar_pokemon_avanzado()
