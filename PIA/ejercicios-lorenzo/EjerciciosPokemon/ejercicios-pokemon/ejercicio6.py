import requests
import os


def descargar_sprites():
    print("¡Descarga los sprites de varios Pokémon!")

    # Crear carpeta para guardar las imágenes si no existe
    carpeta_sprites = "sprites_pokemon"
    os.makedirs(carpeta_sprites, exist_ok=True)

    # Solicitar nombres de Pokémon al usuario
    nombres_pokemones = input("Ingresa nombres de Pokémon separados por comas: ").strip().lower()
    lista_nombres = [nombre.strip() for nombre in nombres_pokemones.split(",")]

    for nombre in lista_nombres:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
        try:
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                sprite_url = datos['sprites']['front_default']  # URL del sprite
                if sprite_url:
                    # Descargar la imagen
                    imagen_respuesta = requests.get(sprite_url)
                    nombre_archivo = os.path.join(carpeta_sprites, f"{nombre}.png")

                    # Guardar la imagen localmente
                    with open(nombre_archivo, "wb") as archivo:
                        archivo.write(imagen_respuesta.content)

                    print(f"Sprite de '{nombre}' descargado y guardado en '{nombre_archivo}'")
                else:
                    print(f"No se encontró un sprite para '{nombre}'.")
            else:
                print(f"Error: No se encontró el Pokémon '{nombre}' (código {respuesta.status_code}).")

        except requests.ConnectionError:
            print("Error: No hay conexión a Internet.")
            break
        except Exception as e:
            print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    descargar_sprites()
