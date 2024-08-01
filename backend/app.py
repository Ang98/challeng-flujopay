from flask import Flask, jsonify, request, abort
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, decode_token
import json
import os

app = Flask(__name__)

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esto por una clave secreta fuerte
jwt = JWTManager(app)

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Cliente API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

DATA_FILE = 'clientes.json'

def read_data():
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/clientes', methods=['GET'])
@jwt_required()
def get_clientes():
    clientes = read_data()
    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['GET'])
@jwt_required()
def get_cliente(id):
    clientes = read_data()
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente is None:
        abort(404)
    return jsonify(cliente)

@app.route('/clientes', methods=['POST'])
@jwt_required()
def create_cliente():
    cliente = request.get_json()
    clientes = read_data()
    if any(c['id'] == cliente['id'] for c in clientes):
        abort(400, 'Cliente with this ID already exists')
    clientes.append(cliente)
    write_data(clientes)
    return jsonify(cliente), 201

@app.route('/clientes/<int:id>', methods=['PUT'])
@jwt_required()
def update_cliente(id):
    cliente_data = request.get_json()
    clientes = read_data()
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente is None:
        abort(404)
    cliente.update(cliente_data)
    write_data(clientes)
    return jsonify(cliente)

@app.route('/clientes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_cliente(id):
    clientes = read_data()
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente is None:
        abort(404)
    clientes.remove(cliente)
    write_data(clientes)
    return '', 204

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    username = auth.get('username')
    password = auth.get('password')

    # Aquí deberías verificar el usuario y la contraseña con una base de datos real.
    # Para este ejemplo, estamos usando datos de prueba.
    if username != 'admin' or password != 'password':
        abort(401, 'Invalid credentials')

    access_token = create_access_token(identity={'username': username})
    return jsonify(access_token=access_token), 200

if __name__ == '__main__':
    app.run(debug=True)
