from app import app
from flask import render_template,request,jsonify

@app.route('/Home/index',methods=['GET', 'POST'])#funcion que retorna la vista
def IndexHome():
	return render_template('Home/index.html')