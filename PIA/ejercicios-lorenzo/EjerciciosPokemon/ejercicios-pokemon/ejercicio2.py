import requests

def obtener_n_pokemon():
    try:
        # Solicitar el número de Pokémon a listar
        limite = int(input("¿Cuántos Pokémon quieres listar? (Introduce un número): "))
        if limite <= 0:
            print("Error: El número debe ser mayor que 0.")
            return

        # URL de la API con el parámetro 'limit'
        url = f"https://pokeapi.co/api/v2/pokemon?limit={limite}"

        # Realizar la solicitud GET a la API
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            pokemones = datos['results']

            # Mostrar los Pokémon obtenidos
            print(f"\nLista de los primeros {limite} Pokémon:")
            for i, pokemon in enumerate(pokemones, start=1):
                print(f"{i}. Nombre: {pokemon['name'].capitalize()} - URL: {pokemon['url']}")
            print()

        else:
            print("\nError: No se pudo obtener la lista de Pokémon del servidor.\n")

    except requests.ConnectionError:
        print("\nError: No se pudo establecer conexión a Internet.\n")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {str(e)}\n")

# Ejecutar la función
if __name__ == "__main__":
    obtener_n_pokemon()
