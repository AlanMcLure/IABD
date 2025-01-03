import requests
import subprocess
import json

def comparar_curl_python():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"

    # --- Solicitud con curl ---
    print("Realizando solicitud con curl...")
    try:
        resultado_curl = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        datos_curl = json.loads(resultado_curl.stdout)  # Convertir la salida JSON de curl a un diccionario
        print("Solicitud con curl completada.")
    except Exception as e:
        print(f"Error ejecutando curl: {e}")
        return

    # --- Solicitud con Python ---
    print("Realizando solicitud con Python (requests)...")
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos_python = respuesta.json()
            print("Solicitud con Python completada.")
        else:
            print(f"Error en la solicitud con Python: Código {respuesta.status_code}")
            return
    except Exception as e:
        print(f"Error con Python requests: {e}")
        return

    # --- Comparar resultados ---
    print("\nComparando resultados entre curl y Python...")
    if datos_curl == datos_python:
        print("✅ Los resultados son consistentes entre curl y Python.")
    else:
        print("❌ Los resultados difieren entre curl y Python.")
        print("\nResultados con curl:")
        print(json.dumps(datos_curl, indent=4))
        print("\nResultados con Python:")
        print(json.dumps(datos_python, indent=4))

if __name__ == "__main__":
    comparar_curl_python()
