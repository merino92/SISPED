from conexion.conexion import Base
from flask import jsonify
import json
import psycopg2
from  psycopg2.extras  import  RealDictCursor 
import datetime 

class Paciente():

	def Listar(self):
		cadena=Base()
		cad=cadena.Conexion()
		cur=cad.cursor(cursor_factory = RealDictCursor)
		cur.execute("SELECT * FROM PUBLIC.pacientes")
		
		rows=cur.fetchall()
		
		cad.close()
		f=Paciente()
		obj=json.dumps(rows,default=f.ConvertirFecha)
		print(obj)
		return  obj

	def ConvertirFecha(self,fecha):
		
		f=Paciente()
		return "{}-{}-{}".format(f.AgregarCero(fecha.day),f.AgregarCero(fecha.month), fecha.year)
	
	def AgregarCero(self,fecha):
		if(fecha>10):
			res=0+fecha
			return res