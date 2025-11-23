from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

productos = []

@app.route('/')
def home():
    return 'API de Productos Médicos 🩺'

@app.route('/productos', methods=['GET', 'POST'])
def productos_lista():
    if request.method == 'POST':
        json = request.get_json()
        json['id'] = len(productos) + 1
        productos.append(json)
        return {
            'ok': True,
            'message': 'Producto creado correctamente',
            'data': json
        }, 200

    elif request.method == 'GET':
        return {
            'ok': True,
            'message': 'Lista de productos obtenida correctamente',
            'data': productos
        }, 200

if __name__ == '__main__':
    app.run(debug=True)