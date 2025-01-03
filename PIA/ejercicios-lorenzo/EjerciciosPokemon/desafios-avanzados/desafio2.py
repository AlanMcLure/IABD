import subprocess
import json

def generar_y_ejecutar_curl():
    print("Automatización de solicitudes curl...")
    # Solicitar al usuario una lista de Pokémon
    nombres_pokemon = input("Ingresa los nombres de los Pokémon separados por comas (ej: pikachu,charmander,bulbasaur): ")
    lista_pokemon = [nombre.strip() for nombre in nombres_pokemon.split(",")]

    print("\nGenerando y ejecutando comandos curl...")
    for nombre in lista_pokemon:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
        comando_curl = ["curl", "-s", url]

        print(f"\nObteniendo datos para: {nombre} (comando: curl -s {url})")
        try:
            # Ejecutar el comando curl
            resultado = subprocess.run(comando_curl, capture_output=True, text=True)
            if resultado.stdout:
                datos = json.loads(resultado.stdout)
                print(f"Nombre: {datos['name']}")
                print(f"Altura: {datos['height']}")
                print(f"Peso: {datos['weight']}")
                print(f"Habilidades: {[h['ability']['name'] for h in datos['abilities']]}")
            else:
                print(f"❌ No se pudo obtener información para '{nombre}'.")
        except json.JSONDecodeError:
            print(f"❌ La respuesta para '{nombre}' no es válida (¿nombre incorrecto?).")
        except Exception as e:
            print(f"❌ Error al ejecutar curl: {e}")

if __name__ == "__main__":
    generar_y_ejecutar_curl()
