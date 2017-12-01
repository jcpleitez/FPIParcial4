import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///gym.db')
app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

class SucursalLogin(Resource):
    def post(self):
        conn = db_connect.connect()
        try:
            contra = request.json['contrasenaSucursal']
            user = request.json['userSucursal']
            textQuery = "select * from sucursales where userSucursal =? and contrasenaSucursal=?"
            query = conn.execute(textQuery, (user, contra))
            for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
            print "OK JSON POST login in sucursales"
            return jsonify(result)
        except:
            print "Bad JSON POST login in sucursales"
            status = None
        return status

class Sucursales(Resource):
   def get(self):
       conn = db_connect.connect() # connect to database
       query = conn.execute("select * from sucursales") # This line performs que$
       result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
       return jsonify(result)

   def post(self):
        conn = db_connect.connect()
        try:
            activo = request.json['activoSucursal']
            contra = request.json['contrasenaSucursal']
            direc = request.json['direccionSucursal']
            idS = request.json['idSucursal']
            idS = 0
            user = request.json['userSucursal']
            nombre = request.json['nombreSucursal']
            telefono = request.json['telefonoSucursal']
            textInsert = "insert into sucursales(nombreSucursal, userSucursal, direccionSucursal, telefonoSucursal, activoSucursal, contrasenaSucursal) VALUES(?,?,?,?,?,?)"
            query = conn.execute(textInsert, (nombre, user, direc, telefono, activo, contra))
            print "OK new POST in sucursales"
            status = True
        except:
            print "Bad JSON POST in sucursales"
            status = False

        return status

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

    def post(self):
         conn = db_connect.connect()
         try:
             #Verificar sucursal
             idS = request.json['idSucursal']
             querySucural = conn.execute("select * from sucursales where idSucursal =%d "  %int(idS))
             idS = querySucural.fetchone()[0]
             #Datos miembro
             idM = request.json['idMiembro']
             idM = 0
             nombre = request.json['nombreMiembro']
             apellido = request.json['apellidoMiembro']
             telefono = request.json['telefonoMiembro']
             activo = request.json['activoMiembro']
             textInsert = "insert into miembros(idSucursal, nombreMiembro, apellidoMiembro, telefonoMiembro, activoMiembro) VALUES(?,?,?,?,?)"
             query = conn.execute(textInsert, (idS, nombre, apellido, telefono, activo))
             print "OK new POST in miembros"
             status = True
         except:
             print "Bad JSON POST in miembros"
             status = False

         return status

class MiembrosSucursal(Resource):
    def get(self, idSucursal):
        conn = db_connect.connect()
        try:
            query = conn.execute("select * from miembros where activoMiembro=1 and idSucursal =%d "  %int(idSucursal))
            miembros = []
            for i in query.cursor: miembros.append(dict(zip(tuple (query.keys()) ,i)))
            print "OK GET  miembros activos por sucursales"
            return jsonify(miembros)
        except:
            return False

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

    def post(self):
         conn = db_connect.connect()
         try:
             #Verificar sucursal
             idS = request.json['idSucursal']
             querySucural = conn.execute("select * from sucursales where idSucursal =%d "  %int(idS))
             idS = querySucural.fetchone()[0]
             #Datos empleados
             idE = request.json['idEmpleado']
             idE = 0
             nombre = request.json['nombreEmpleado']
             apellido = request.json['apellidoEmpleado']
             telefono = request.json['telefonoEmpleado']
             activo = request.json['activoEmpleado']
             textInsert = "insert into empleados(idSucursal, nombreEmpleado, apellidoEmpleado, telefonoEmpleado, activoEmpleado) VALUES(?,?,?,?,?)"
             query = conn.execute(textInsert, (idS, nombre, apellido, telefono, activo))
             print "OK new POST in empleados"
             status = True
         except:
             print "Bad JSON POST in empleados"
             status = False

         return status

class EmpleadosSucursal(Resource):
    def get(self, idSucursal):
        conn = db_connect.connect()
        try:
            query = conn.execute("select * from empleados where activoEmpleado=1 and idSucursal =%d "  %int(idSucursal))
            empleados = []
            for i in query.cursor: empleados.append(dict(zip(tuple (query.keys()) ,i)))
            print "OK GET  empleados activos por sucursales"
            return jsonify(empleados)
        except:
            return False

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

    def post(self):
         conn = db_connect.connect()
         try:
             #Verificar empleado
             idE = request.json['idEmpleado']
             queryE = conn.execute("select * from empleados where idEmpleado =%d "  %int(idE))
             idE = queryE.fetchone()[0]
             #Verificar miembro
             idM = request.json['idMiembro']
             queryM = conn.execute("select * from miembros where idMiembro =%d "  %int(idM))
             idM = queryM.fetchone()[0]
             #Verificar sucursal
             idS = request.json['idSucursal']
             queryS = conn.execute("select * from sucursales where idSucursal =%d "  %int(idS))
             idS = queryS.fetchone()[0]
             #Verificar tipo pago
             idTP = request.json['idTipoPago']
             queryTP = conn.execute("select * from tipoPago where idTipoPago =%d "  %int(idTP))
             idTP = queryTP.fetchone()[0]
             #Fecha
             fecha = request.json['datePago']
             fecha = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
             #Verificar que no existes un pago igual idPago
             idP = request.json['idPago']
             #Contarlos para validar que no tenga una matricula
             queryCantidadPagos = conn.execute("select count(idPago) from pagos where idTipoPago=1 and idMiembro=%d "  %int(idM))
             cantidaPagos = queryCantidadPagos.fetchone()[0]

             if idTP==1:
                 if cantidaPagos==0:
                     textInsert = "insert into pagos(idTipoPago, idMiembro, idEmpleado, idSucursal, datePago) VALUES(?,?,?,?,?)"
                     query = conn.execute(textInsert, (idTP, idM, idE, idS, fecha))
                     print "OK new POST Mensualidad in pagos"
                     status = True
                 else:
                     print "Miembro ya tiene matricula"
                     status = False
             else:
                 textInsert = "insert into pagos(idTipoPago, idMiembro, idEmpleado, idSucursal, datePago) VALUES(?,?,?,?,?)"
                 query = conn.execute(textInsert, (idTP, idM, idE, idS, fecha))
                 print "OK new POST Mensualidad in pagos"
                 status = True

         except:
             print "Bad JSON POST in pagos"
             status = False

         return status

class PagosMiembro(Resource):
    def get(self, idMiembro):
        conn = db_connect.connect() # connect to database
        try:
            queryM = conn.execute("select * from miembros where idMiembro =%d "  %int(idMiembro))
            idM = queryM.fetchone()[0]
            query = conn.execute("select * from pagos where idMiembro =%d "  %int(idMiembro))
            result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
            print "Get pagos del miembro"
            return jsonify(result)
        except:
            print "No existe miembro"
            return None


class PagosID(Resource):
    def get(self, idPago):
        conn = db_connect.connect()
        query = conn.execute("select * from pagos where idPago =%d "  %int(idPago))
        for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
        return jsonify(result)

class MiembroEnabled(Resource):
    def post(self):
         conn = db_connect.connect()
         try:
             #Verificar Miembro
             idM = request.json['idMiembro']
             queryM = conn.execute("select * from miembros where idMiembro =%d" %int(idM))
             idM = queryM.fetchone()[0]
             activo = request.json['activoMiembro']
             if activo>0:
                 activo = 1
             textEnable = "update miembros set activoMiembro=? where idMiembro =%d " %int(idM)
             query = conn.execute(textEnable, activo)
             print "OK se ha edito el estado de activo del miembro"
             status = True
         except:
             print "Bad JSON POST in Soft-Delete"
             status = False

         return status


api.add_resource(SucursalLogin, '/login') # Direccion sucursales
api.add_resource(Sucursales, '/sucursales') # Direccion sucursales
api.add_resource(SucursalesID, '/sucursales/<idSucursal>') # Direccion de sucursal id
api.add_resource(Miembros, '/miembros') # Direccion de miembos
api.add_resource(MiembrosSucursal, '/miembros/sucursal/<idSucursal>') # Direccion de miembos id
api.add_resource(MiembrosID, '/miembros/<idMiembro>') # Direccion de miembos id
api.add_resource(MiembroEnabled, '/miembros/estado') # Direccion de miembos id
api.add_resource(Empleados, '/empleados') # Direccion de empleados
api.add_resource(EmpleadosSucursal, '/empleados/sucursal/<idSucursal>') # Direccion de miembos id
api.add_resource(EmpleadosID, '/empleados/<idEmpleado>') # Direccion de empleados id
api.add_resource(TipoPagos, '/tipoPagos') # Direccion de tipo pago
api.add_resource(TipoPagosID, '/tipoPagos/<idTipoPago>') # Direccion de tipo pago
api.add_resource(Pagos, '/pagos') # Direccion de pagos
api.add_resource(PagosMiembro, '/pagos/miembro/<idMiembro>') # Direccion de pagos
api.add_resource(PagosID, '/pagos/<idPago>') # Direccion de pagos

if __name__ == '__main__':
     app.run(host='0.0.0.0')
     app.run(port='5000')
