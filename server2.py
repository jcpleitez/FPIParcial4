import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///gym.db')
app = Flask(__name__)
api = Api(app)

class Sucursales(Resource):
   def get(self):
       conn = db_connect.connect() # connect to database
       query = conn.execute("select * from sucursales") # This line performs que$
       result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
       return jsonify(result)

class SucursalesID(Resource):
   def get(self, idSucursal):
       conn = db_connect.connect() # connect to database
       query = conn.execute("select * from sucursales where idSucursal =%d "  %int(idSucursal))
       for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
       return jsonify(result)

class Miembros(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
    	query = conn.execute("select * from miembros") # This line performs query and returns json result
    	miembros = []
    	for i in query.cursor: miembros.append(dict(zip(tuple (query.keys()) ,i)))
        return jsonify(miembros)

class MiembrosID(Resource):
    def get(self, idMiembro):
        conn = db_connect.connect()
        query = conn.execute("select * from miembros where idMiembro =%d "  %int(idMiembro))
        for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
        return jsonify(result)

class Empleados(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
    	query = conn.execute("select * from empleados") # This line performs query and returns json result
    	empleados = []
    	for i in query.cursor: empleados.append(dict(zip(tuple (query.keys()) ,i)))
        return jsonify(empleados)

class EmpleadosID(Resource):
    def get(self, idEmpleado):
        conn = db_connect.connect()
        query = conn.execute("select * from empleados where idEmpleado =%d "  %int(idEmpleado))
        for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
        return jsonify(result)

class TipoPagos(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from tipoPago") # This line performs q$
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

class TipoPagosID(Resource):
    def get(self, idTipoPago):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from tipoPago where idTipoPago =%d "  %int(idTipoPago))
        for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
        return jsonify(result)

class Pagos(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from pagos") # This line performs q$
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

class PagosID(Resource):
    def get(self, idPago):
        conn = db_connect.connect()
        query = conn.execute("select * from pagos where idPago =%d "  %int(idPago))
        for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
        return jsonify(result)


api.add_resource(Sucursales, '/sucursales') # Direccion sucursales
api.add_resource(SucursalesID, '/sucursales/<idSucursal>') # Direccion de sucursal id
api.add_resource(Miembros, '/miembros') # Direccion de miembos
api.add_resource(MiembrosID, '/miembros/<idMiembro>') # Direccion de miembos id
api.add_resource(Empleados, '/empleados') # Direccion de empleados
api.add_resource(EmpleadosID, '/empleados/<idEmpleado>') # Direccion de empleados id
api.add_resource(TipoPagos, '/tipoPagos') # Direccion de tipo pago
api.add_resource(TipoPagosID, '/tipoPagos/<idTipoPago>') # Direccion de tipo pago
api.add_resource(Pagos, '/pagos') # Direccion de pagos
api.add_resource(PagosID, '/pagos/<idPago>') # Direccion de pagos

if __name__ == '__main__':
     app.run(host='0.0.0.0')
     app.run(port='5002')
