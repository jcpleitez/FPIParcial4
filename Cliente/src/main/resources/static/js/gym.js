var ipDomain = "http://192.168.0.28:5000/";

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
