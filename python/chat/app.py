from flask import Flask,render_template
from flask_socketio import SocketIO,send,emit
import serial,time
app=Flask(__name__)

app.config['SECRET KEY']='12345'
app.debug=True

from controllers.LoginController import *
from controllers.HomeController import *
from controllers.PacienteController import *
socket=SocketIO(app)


@socket.on('mensaje')
def Mensaje (vale):
	print(vale)
	arduino =serial.Serial('COM3',9600)
	time.sleep(2)
	arduino.write(b'9')
	#('mensaje',men,broadcast=True)
	arduino.close()

if __name__ == '__main__':

	socket.run(app,host='0.0.0.0',port=8081)