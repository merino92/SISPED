import psycopg2

class Base:
	"""docstring for ClassName __init__(self, arg):
		super(ClassName__init__()
		self.arg = arg
	"""
	def Conexion(self):
		con=psycopg2.connect(host='localhost',user='postgres',password='admin',database='SALUD')

		return con