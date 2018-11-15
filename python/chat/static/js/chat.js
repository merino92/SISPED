$(document).ready(function(){


Cargar();

});


function Cargar(){

	var socket = io.connect('http://localhost:8081');
	socket.on('connect', function() {
		
		socket.emit('hola mundo');
		console.log("conectado");
	});
	
	

	$('#presionar').on('click', function() {
		socket.emit('mensaje',$('#caja').val());

		$('#caja').val('');

	}); 

	socket.on('mensaje',function(msg) {
		console.log("hola mundo:"+msg);
		$("#men").append('<li>'+msg+'</li>');
		
		
	});
}


