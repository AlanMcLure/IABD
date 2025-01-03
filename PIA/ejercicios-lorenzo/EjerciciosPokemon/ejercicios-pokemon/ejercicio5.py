import requests

def obtener_movimientos_pokemon():
    print("¡Consulta los movimientos de un Pokémon!")

    # Solicitar el nombre del Pokémon
    nombre_pokemon = input("Ingresa el nombre de un Pokémon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    try:
        # Solicitar datos del Pokémon
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            movimientos = [movimiento['move']['name'] for movimiento in datos['moves']]

            # Imprimir la lista de movimientos
            print(f"\nMovimientos de '{nombre_pokemon.capitalize()}':")
            for movimiento in movimientos:
                print(f"- {movimiento}")
            print()

        elif respuesta.status_code == 404:
            print("\nError: El Pokémon no fue encontrado.\n")
        else:
            print("\nError: No se pudo obtener la información del servidor.\n")

    except requests.ConnectionError:
        print("\nError: No hay conexión a Internet.\n")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}\n")

# Ejecutar la función
if __name__ == "__main__":
    obtener_movimientos_pokemon()
