from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///gym.db')
app = Flask(__name__)
api = Api(app)

class Miembros(Resource):
    def get(self):
	conn = db_connect.connect() # connect to database
	query = conn.execute("select * from miembros") # This line performs query and returns json result
	result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

class MiembrosID(Resource):
    def get(self, id_Miembro):
        conn = db_connect.connect()
        query = conn.execute("select * from miembros where idMiembro =%d "  %int(id_Miembro))
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

class Sucursales(Resource):
   def get(self):
	conn = db_connect.connect() # connect to database
        query = conn.execute("select * from sucursales") # This line performs que$
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

class TipoPago(Resource):
   def get(self):
	conn = db_connect.connect() # connect to database
        query = conn.execute("select * from tipoPago") # This line performs q$
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

class Pagos(Resource):
   def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from pagos") # This line performs q$
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)


api.add_resource(Miembros, '/miembros') # Direccion de miembos
api.add_resource(MiembrosID, '/miembros/<id_Miembro>') # Direccion de miembos
api.add_resource(Sucursales, '/sucursales') # Direccion sucursales
api.add_resource(TipoPago, '/tipoPago') # Direccion de tipo pago
api.add_resource(Pagos, '/pagos') # Direccion de pagos


if __name__ == '__main__':
     app.run(host='0.0.0.0')
     app.run(port='5002')
