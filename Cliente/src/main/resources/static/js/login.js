var ipDomain = "http://192.168.43.46:5000/";

function verificarCookie(){
	if(document.cookie.length!==0){
		location.href = "index";
	}
}
setInterval(function(){verificarCookie()},1000);

document.getElementById("login").onsubmit = function(e){
  e.preventDefault(e);
  var pas = document.getElementById("contraSucursal").value;
  var user = document.getElementById("userSucursal").value;
  var data = {"contrasenaSucursal":pas, "userSucursal":user};
  $.ajax({
    url        : ipDomain+'login',
    dataType   : 'json',
    contentType: 'application/json; charset=UTF-8',
    data       : JSON.stringify(data),
    type       : 'POST',
    }).done(function(response) {
        if (response != null) {
          var date = new Date();
          date.setTime(date.getTime() + (24 * 60 * 60 * 1000));
		      var expires = "; expires="+date.toGMTString();
		      document.cookie = "sucursal="+response.idSucursal+expires;
          new PNotify({
            title: 'Aviso',
            text: 'Ha Iniciado: '+response.nombreSucursal
          });
          location.href = "index";
          }else {
            new PNotify({
              title: 'Oh No!',
              text: 'Error en usuario o contraseña',
              type: 'error'
            });
          }
      });
}
