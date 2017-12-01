var ipDomain = "http://192.168.1.9:5000/";

$(document).ready(function(){
  var sucursalSelect =  document.getElementById('sucursales').value;
  CargarMiembros(sucursalSelect);
});

$("#sucursales").change(function () {
  var sucursalSelect =  document.getElementById('sucursales').value;
  CargarMiembros(sucursalSelect);
});

function CargarMiembros(idSucursal) {
  $.ajax({
  url: ipDomain+"miembros/sucursal/"+idSucursal,
  dataType: 'json',
  type: 'GET',
  }).done(function(response) {
    $("#miembros").html("");
    $.each(response, function(i){
      var option = $('<option>'+response[i].nombreMiembro+" "+response[i].apellidoMiembro+'</option>').attr('value',response[i].idMiembro);
      $("#miembros").append(option);
    });
  });
}
//////////////////////////////////Para el POST////////////////////////////////////////////////////////
document.getElementById("addMember").onsubmit = function(e){
  e.preventDefault();
  var idSucursal = document.cookie.split(";")[0].split("=")[1];
  var name = document.getElementById("addMemberName");
  var lastname = document.getElementById("addMemberLastName");
  var phone = document.getElementById("addMemberPhone");
  var data = {"activoMiembro":1, "apellidoMiembro":lastname.value, "idMiembro":0, "idSucursal":idSucursal, "nombreMiembro":name.value, "telefonoMiembro":phone.value};
  $.ajax({
    url        : ipDomain+'miembros',
    dataType   : 'json',
    contentType: 'application/json; charset=UTF-8', // This is the money shot
    data       : JSON.stringify(data),
    type       : 'POST',
    }).done(function(response) {
        if (response) {
          new PNotify({
            title: 'Éxito',
            text: 'Se ha registrado un nuevo miembro con exito',
            type: 'success'
          });
        }else {
          new PNotify({
            title: 'Oh No!',
            text: 'Ha ocurrido un error al registrar',
            type: 'error'
          });
        }
      });
}
//////////////////////////////////"Eliminar" miembro////////////////////////////////////////////
function Eliminar(idMiembro) {
  var data = {"activoMiembro":0, "idMiembro":idMiembro};
  $.ajax({
    url        : ipDomain+'miembros/estado',
    dataType   : 'json',
    contentType: 'application/json; charset=UTF-8', // This is the money shot
    data       : JSON.stringify(data),
    type       : 'POST',
    }).done(function(response) {
        if (response) {
          new PNotify({
            title: 'Éxito',
            text: 'Se ha eliminado al miembro con exito',
            type: 'success'
          });
          location.href = "index";
        }else {
          new PNotify({
            title: 'Oh No!',
            text: 'Ha ocurrido un error al eliminar',
            type: 'error'
          });
        }
      });

}
///////////////////////////////////POST para pagos Matricula//////////////////////////////////////
document.getElementById("pagoMatricula").onsubmit = function(e){
  e.preventDefault();
  var idEmpleado = document.getElementById("empleados");
  var idSucursal = document.getElementById("sucursales");
  var idMiembro = document.getElementById("miembros");
  var tipoPago = 1;
  var data = {"datePago":"Now", "idEmpleado":idEmpleado.value, "idMiembro":idMiembro.value, "idPago":0, "idSucursal":idSucursal.value, "idTipoPago":tipoPago};
  $.ajax({
    url        : ipDomain+'pagos',
    dataType   : 'json',
    contentType: 'application/json; charset=UTF-8', // This is the money shot
    data       : JSON.stringify(data),
    type       : 'POST',
    }).done(function(response) {
        if (response) {
          new PNotify({
            title: 'Éxito',
            text: 'Se ha pagado la matrícula con exito',
            type: 'success'
          });
        }else {
          new PNotify({
            title: 'Oh No!',
            text: 'Ha ocurrido un error al pagar',
            type: 'error'
          });
        }
      });
}
///////////////////////////////////POST para pagos Mensualidad//////////////////////////////////////
document.getElementById("pagoMensualidad").onsubmit = function(e){
  e.preventDefault();
  var idEmpleado = document.getElementById("empleados");
  var idSucursal = document.getElementById("sucursales");
  var idMiembro = document.getElementById("miembros");
  var tipoPago = 2;
  var data = {"datePago":"Now", "idEmpleado":idEmpleado.value, "idMiembro":idMiembro.value, "idPago":0, "idSucursal":idSucursal.value, "idTipoPago":tipoPago};
  $.ajax({
    url        : ipDomain+'pagos',
    dataType   : 'json',
    contentType: 'application/json; charset=UTF-8', // This is the money shot
    data       : JSON.stringify(data),
    type       : 'POST',
    }).done(function(response) {
        if (response) {
          new PNotify({
            title: 'Éxito',
            text: 'Se ha pagado la mensualidad con exito',
            type: 'success'
          });
        }else {
          new PNotify({
            title: 'Oh No!',
            text: 'Ha ocurrido un error al pagar',
            type: 'error'
          });
        }
      });
}
////////////////////////////////////////Modal para ver pagos///////////////////////////////////////////////////
function ActivarModal(idMiembro){
  $("#valoresTabla").html("");
	var codigo;
	var fecha;
	var nombre;
	var apellido;
	var sucursal;
	var empleado;
	var tipoPago;
  $.ajax({
  url: ipDomain+"pagos/miembro/"+idMiembro,
  dataType: 'json',
  type: 'GET',
  }).done(function(response) {
    $.each(response, function(i){

      $.ajax({
      url: ipDomain+"miembros/"+response[i].idMiembro,
      dataType: 'json',
      type: 'GET',
    }).done(function(response1) {
          nombre=response1.nombreMiembro;
          apellido=response1.apellidoMiembro;
          $.ajax({
          url: ipDomain+"sucursales/"+response[i].idSucursal,
          dataType: 'json',
          type: 'GET',
        }).done(function(response2) {
              sucursal=response2.nombreSucursal;
              $.ajax({
              url: ipDomain+"empleados/"+response[i].idEmpleado,
              dataType: 'json',
              type: 'GET',
            }).done(function(response3) {
                  empleado=response3.nombreEmpleado +" "+response3.apellidoEmpleado;
                  $.ajax({
                  url: ipDomain+"tipoPagos/"+response[i].idTipoPago,
                  dataType: 'json',
                  type: 'GET',
                  }).done(function(response4) {
                      tipoPago=response4.nombreTipoPago;
                	  codigo=response[i].idPago;
                      fecha=response[i].datePago;
                      var tr = $('<tr><td>'+codigo+'</td><td>'+nombre+'</td><td>'+apellido+'</td><td>'+sucursal+'</td><td>'+tipoPago+'</td><td>'+empleado+'</td><td>'+fecha+'</td></tr>');
                      $("#valoresTabla").append(tr);
                  });
              });
          });
      });
    });
  });
  $("#myModalPagos").modal();
}
//////////////////////////////////Manejando la cookie/////////////////////////////////////////////////
function LogOut() {
	document.cookie = "sucursal=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
}
function verificarCookie(){
	if(document.cookie.length==0){
    new PNotify({
      title: 'Aviso',
      text: 'Se cerrará la sesión'
    });
		location.href = "login";
	}
}
setInterval(function(){verificarCookie()},1000);

////////////////////////////////////Codigo del tema de la vista////////////////////////////////////////////
(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#sideNav'
  });

})(jQuery); // End of use strict
