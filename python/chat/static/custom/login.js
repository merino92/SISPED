$(document).ready(function(){

}); 


function Loguear(){
var objecto={

	usuario:$("#usuario").val(),
	clave:$("#clave").val()
};
 $.ajax({
        url: "/Login/loguear",
        type: "POST",
        data:JSON.stringify(objecto),
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        success: function (result) {
                console.log(result);
        	if(result.length > 0){
                    location.href ='/Home/index';
            }else{

                alert("INVALIDO");
            }
            
        },
        error: function (errormessage) {
            alert(errormessage.responseText);
        }
    }).done(function () {

    });

}