import requests
import json


def guardar_pokemon_json():
    print("Guardando datos de los primeros 10 Pokémon en un archivo JSON...\n")

    url_base = "https://pokeapi.co/api/v2/pokemon"
    limit = 10  # Obtener solo los primeros 10 Pokémon
    archivo_salida = "pokemon_data.json"
    datos_pokemon = []

    try:
        # Obtener la lista de los primeros 10 Pokémon
        parametros = {"limit": limit, "offset": 0}
        respuesta = requests.get(url_base, params=parametros)

        if respuesta.status_code == 200:
            resultados = respuesta.json().get('results', [])

            for pokemon in resultados:
                # Obtener detalles individuales de cada Pokémon
                respuesta_detalle = requests.get(pokemon['url'])
                if respuesta_detalle.status_code == 200:
                    datos = respuesta_detalle.json()

                    nombre = datos['name']
                    tipos = [tipo['type']['name'] for tipo in datos['types']]
                    habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]

                    datos_pokemon.append({
                        "name": nombre,
                        "types": tipos,
                        "abilities": habilidades
                    })
                    print(f"Datos de '{nombre}' obtenidos correctamente.")
                else:
                    print(f"Error al obtener detalles de '{pokemon['name']}'.")

            # Guardar en archivo JSON
            with open(archivo_salida, "w") as archivo:
                json.dump(datos_pokemon, archivo, indent=4)

            print(f"\nDatos guardados en '{archivo_salida}'.")
        else:
            print(f"Error al obtener la lista de Pokémon (código {respuesta.status_code}).")

    except requests.ConnectionError:
        print("Error: No hay conexión a Internet.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    guardar_pokemon_json()
