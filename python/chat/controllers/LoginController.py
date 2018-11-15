from app import app
from flask import render_template,request,jsonify
from repository.loginRepository import *


@app.route('/',methods=['GET', 'POST'])#funcion que retorna la vista
def Index():
	return render_template('login/login.html')

@app.route('/Login/loguear',methods=['POST'])
def Logueo():
	res=request.get_json()
	l=Login()
	dato=l.Loguear(res)
	print("datos:"+dato)
	return  dato


		