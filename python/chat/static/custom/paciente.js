$(document).ready(function(){

Listar();
socket= io.connect('http://localhost:8081');
}); 
var socket;
function Listar(){

	$.ajax({
        url: "/Paciente/listar",
        type: "GET",
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        success: function (result) {
        	var html="";
            console.log(result);
            $.each(result,function(i,item){
            	var apellidos=item.primer_apellido;
                console.log(item.segundo_apellido);
            	if(item.segundo_apellido!=null){
                    console.log("noes nulo:"+item.segundo_apellido);
            		apellidos=item.primer_apellido+" "+item.segundo_apellido;
            	}
            html+='<tr id='+item.idpacientes+' >';
             html+='<td>'+item.num_expediente+'</td>';
            html+='<td>'+item.nombres+'</td>';
            html+='<td>'+apellidos+'</td>';
            html+='<td>'+item.fecha_nacimiento+'</td>';
         	 html += '<td><a href="#" onclick="Editar(' + item.idpacientes + ')">Editar</a> | <a href="#" onclick="Delete(' + item.idpacientes + ')">Eliminar</a></td>';
            html+='</tr>';

            });

            $("#cuerpo_paciente").html(html);
             $('#tabla_paciente').DataTable();
            
        },
        error: function (errormessage) {
            alert(errormessage.responseText);
        }
    }).done(function () {

    });
} 

function Nuevo(){

   socket.emit('mensaje', "hola");

}