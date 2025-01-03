import requests

def obtener_estadisticas_pokemon():
    print('Estadísticas completas del pokemon')

    # Solicitar el nombre del pokemon
    nombre_pokemon = input("Ingresa el nombre del pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    try:
        # Solicitar los datos
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()

            # Extraer estadísticas
            estadisticas = {stat['stat']['name']: stat['base_stat'] for stat in datos['stats']}

            # Imprimir el diccionario
            print(f"\nEstadísticas base de '{nombre_pokemon.capitalize()}':")
            print(estadisticas, "\n")

        elif respuesta.status_code == 404:
            print("\nError: El Pokémon no fue encontrado. Verifica el nombre.\n")
        else:
            print("\nError: No se pudo obtener la información del servidor.\n")

    except requests.ConnectionError:
        print("\nError: No hay conexión a Internet.\n")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}\n")

# Ejecutar la función
if __name__ == "__main__":
    obtener_estadisticas_pokemon()