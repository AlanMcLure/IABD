import requests


def listar_pokemones_paginados():
    print("Listando los primeros 100 Pokémon utilizando paginación...\n")

    url_base = "https://pokeapi.co/api/v2/pokemon"
    limit = 20  # Número de Pokémon por página
    total_pokemones = 100  # Objetivo: listar los primeros 100
    offset = 0  # Desplazamiento inicial

    nombres_pokemon = []

    while len(nombres_pokemon) < total_pokemones:
        # Parámetros para la paginación
        parametros = {"limit": limit, "offset": offset}
        try:
            respuesta = requests.get(url_base, params=parametros)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                resultados = datos.get('results', [])

                # Extraer nombres
                for pokemon in resultados:
                    nombres_pokemon.append(pokemon['name'])
                    if len(nombres_pokemon) >= total_pokemones:
                        break

                print(f"Página obtenida (offset={offset}): {', '.join([p['name'] for p in resultados])}")

                # Aumentar offset para la siguiente página
                offset += limit
            else:
                print(f"Error al obtener datos (código {respuesta.status_code}).")
                break

        except requests.ConnectionError:
            print("Error: No hay conexión a Internet.")
            break
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            break

    print("\nLos primeros 100 Pokémon son:")
    for i, nombre in enumerate(nombres_pokemon, 1):
        print(f"{i}. {nombre}")


if __name__ == "__main__":
    listar_pokemones_paginados()
