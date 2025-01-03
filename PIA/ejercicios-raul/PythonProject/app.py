from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)

# Lista inicial de tareas
tareas = [
    {"id": 1, "titulo": "Comprar leche", "completada": False},
    {"id": 2, "titulo": "Estudiar Flask", "completada": False}
]

# Generar un ID único para nuevas tareas
def generar_id():
    return max(tarea['id'] for tarea in tareas) + 1 if tareas else 1

# --- Escenarios Básicos ---

# Listar todas las tareas
@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify({'tareas': tareas}), 200

# Añadir una nueva tarea
@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    datos = request.get_json()

    if not datos or 'titulo' not in datos:
        abort(400, description="Debe incluir un título para la tarea.")

    nueva_tarea = {
        "id": generar_id(),
        "titulo": datos['titulo'],
        "completada": False
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# Borrar una tarea específica
@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def borrar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if not tarea:
        abort(404, description="Tarea no encontrada.")
    tareas.remove(tarea)
    return jsonify({"mensaje": f"Tarea con ID {tarea_id} eliminada."}), 200

# Marcar una tarea como completada
@app.route('/tareas/<int:tarea_id>/completar', methods=['PATCH'])
def completar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if not tarea:
        abort(404, description="Tarea no encontrada.")
    tarea['completada'] = True
    return jsonify(tarea), 200

# --- Funcionalidades Extras ---

'''
# URL de la API
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Realizar la solicitud GET
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")
    print("Habilidades:")
    for ability in data['abilities']:
        print(f"  - {ability['ability']['name']}")
else:
    print(f"Error: {response.status_code}")
'''

# Listar pokemons
url = "https://pokeapi.co/api/v2/pokemon?limit=10"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for pokemon in data['results']:
        print(f"Nombre: {pokemon['name']} - URL: {pokemon['url']}")
else:
    print(f"Error: {response.status_code}")

if response.status_code == 404:
    print("El Pokémon solicitado no existe.")
else:
    print(f"Error: {response.status_code}")

# Editar una tarea específica (cambios parciales o totales)
@app.route('/tareas/<int:tarea_id>', methods=['PUT', 'PATCH'])
def editar_tarea(tarea_id):
    datos = request.get_json()
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if not tarea:
        abort(404, description="Tarea no encontrada.")

    if 'titulo' in datos:
        tarea['titulo'] = datos['titulo']
    if 'completada' in datos:
        tarea['completada'] = datos['completada']
    return jsonify(tarea), 200

# Borrar todas las tareas completadas
@app.route('/tareas/completadas', methods=['DELETE'])
def borrar_tareas_completadas():
    global tareas
    tareas = [tarea for tarea in tareas if not tarea['completada']]
    return jsonify({"mensaje": "Tareas completadas eliminadas."}), 200

# Cambiar el estado de una tarea a "incompleta"
@app.route('/tareas/<int:tarea_id>/incompletar', methods=['PATCH'])
def incompletar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if not tarea:
        abort(404, description="Tarea no encontrada.")
    tarea['completada'] = False
    return jsonify(tarea), 200

API_EXTERNA_URL = "http://10.248.116.55:5000/tareas"

@app.route('/external-tasks', methods=['GET'])
def obtener_tareas_externas():
    try:
        # Realizar la solicitud GET a la API externa
        respuesta = requests.get(API_EXTERNA_URL)

        # Verificar si la solicitud fue exitosa
        if respuesta.status_code != 200:
            abort(500, description="Error al obtener datos de la API externa.")

        # Convertir la respuesta JSON en un objeto Python (lista de tareas)
        tareas_externas = respuesta.json()

        # Filtrar las primeras 10 tareas como ejemplo
        primeras_tareas = tareas_externas[:10]

        return jsonify({
            "mensaje": "Tareas obtenidas de la API externa",
            "tareas": primeras_tareas
        }), 200

    except requests.RequestException as e:
        # Manejo de errores al hacer la solicitud
        abort(500, description=f"Error al conectarse con la API externa: {str(e)}")

# --- Manejo de errores ---

@app.errorhandler(400)
def handle_400(error):
    return jsonify({"error": str(error.description)}), 400

@app.errorhandler(404)
def handle_404(error):
    return jsonify({"error": str(error.description)}), 404

@app.errorhandler(500)
def handle_500(error):
    return jsonify({"error": str(error.description)}), 500

# --- Iniciar el servidor ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
