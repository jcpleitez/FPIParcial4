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
          CleanAddMember();
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
function CleanAddMember() {
  document.getElementById("addMemberName").innerHTML="";
  document.getElementById("addMemberLastName").innerHTML="";
  document.getElementById("addMemberPhone").innerHTML="";
}
function Inactivo() {
  new PNotify({
    title: 'Aviso',
    text: 'Se registro como inactivo'
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
///////////////////////////////////POST para pagos Matricula//////////////////////////////////////
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

  $("#myModalPagos").modal();
}
//////////////////////////////////Manejando la cookie/////////////////////////////////////////////////
function LogOut() {
	document.cookie = "sucursal=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
}
function verificarCookie(){
	if(document.cookie.length==0){
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
