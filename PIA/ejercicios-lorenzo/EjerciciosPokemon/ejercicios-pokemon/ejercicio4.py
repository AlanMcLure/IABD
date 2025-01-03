import requests

def obtener_info_varios_pokemones():
    print("¡Consulta información de varios Pokémon!")

    # Solicitar una lista de nombres de Pokémon separados por comas
    nombres_pokemones = input("Ingresa nombres de Pokémon separados por comas: ").strip().lower()
    lista_nombres = [nombre.strip() for nombre in nombres_pokemones.split(",")]

    for nombre in lista_nombres:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

        try:
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                print(f"\nPokémon: {datos['name'].capitalize()}")
                print(f"  - Altura: {datos['height'] / 10} m")
                print(f"  - Peso: {datos['weight'] / 10} kg")
            else:
                print(f"\nError: No se encontró el Pokémon '{nombre}'.")

        except requests.ConnectionError:
            print("\nError: No hay conexión a Internet.")
            break
        except Exception as e:
            print(f"\nError inesperado: {str(e)}")
            break

# Ejecutar la función
if __name__ == "__main__":
    obtener_info_varios_pokemones()
