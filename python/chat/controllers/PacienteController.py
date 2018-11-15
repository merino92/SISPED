from app import app
from flask import render_template,request,jsonify
from repository.pacienterepository import *

@app.route('/Paciente/index',methods=['GET', 'POST'])#funcion que retorna la vista
def IndexPaciente():
	return render_template('pacientes/index.html')

@app.route('/Paciente/listar',methods=['GET'])	
def ListarPaciente():
	paciente=Paciente()
	res=paciente.Listar()
	return res