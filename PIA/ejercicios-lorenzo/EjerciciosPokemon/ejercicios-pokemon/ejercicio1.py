import requests

def obtener_detalles_pokemon():
    print("¡Bienvenido a la API de Pokémon!")

    # Solicitar nombre del Pokémon al usuario
    nombre_pokemon = input("Ingresa el nombre de un Pokémon: ").strip().lower()

    # URL de la API para el Pokémon específico
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    try:
        # Realizar la solicitud GET a la API
        respuesta = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            datos = respuesta.json()

            # Extraer los detalles requeridos
            nombre = datos['name'].capitalize()
            altura = datos['height']
            peso = datos['weight']
            habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]

            # Mostrar la información
            print(f"\nDetalles del Pokémon '{nombre}':")
            print(f"- Altura: {altura / 10} m")  # Convertir decímetros a metros
            print(f"- Peso: {peso / 10} kg")  # Convertir hectogramos a kilogramos
            print(f"- Habilidades: {', '.join(habilidades)}\n")

        elif respuesta.status_code == 404:
            print("\nError: El Pokémon no fue encontrado. Verifica el nombre e inténtalo de nuevo.\n")
        else:
            print("\nError: No se pudo obtener información del servidor.\n")

    except requests.ConnectionError:
        print("\nError: No se pudo establecer conexión a Internet.\n")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {str(e)}\n")

# Ejecutar la función
if __name__ == "__main__":
    obtener_detalles_pokemon()