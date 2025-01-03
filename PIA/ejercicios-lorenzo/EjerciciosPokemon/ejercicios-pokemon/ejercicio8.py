import requests


def obtener_informacion_pokemon():
    print("¡Consulta información avanzada de un Pokémon por ID!")

    # Solicitar el ID del Pokémon
    try:
        id_pokemon = int(input("Ingresa el ID del Pokémon: ").strip())
        url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"

        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()

            # Extraer información avanzada
            nombre = datos['name']
            tipos = [tipo['type']['name'] for tipo in datos['types']]
            habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]

            # Crear y mostrar el resultado
            info_pokemon = {
                "name": nombre,
                "types": tipos,
                "abilities": habilidades
            }
            print("\nInformación del Pokémon:")
            print(info_pokemon, "\n")

        elif respuesta.status_code == 404:
            print("Error: No existe un Pokémon con el ID proporcionado.")
        else:
            print(f"Error inesperado del servidor (código {respuesta.status_code}).")

    except ValueError:
        print("Error: El ID debe ser un número entero válido.")
    except requests.ConnectionError:
        print("Error: No hay conexión a Internet.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    obtener_informacion_pokemon()
