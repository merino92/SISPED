from conexion.conexion import Base
from flask import jsonify
import json
import psycopg2
from  psycopg2.extras  import  RealDictCursor 
class Login:

	

	def Loguear(self,objecto):
		cadena=Base()
		res=objecto
		cad=cadena.Conexion()
		cur=cad.cursor(cursor_factory = RealDictCursor)
		cur.execute("SELECT * FROM PUBLIC.usuarios where usuario=%s and clave=%s",[res['usuario'],res['clave']])
		
		rows=cur.fetchall()
		cad.close()
		obj=json.dumps(rows)
		
		return  obj

