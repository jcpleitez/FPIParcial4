 document.getElementById("login").onsubmit = function(e){
  e.preventDefault(e);
  var data = {"contrasenaSucursal": document.getElementById("#contraSucursal").value, "userSucursal": document.getElementById("#userSucursal").value};
  $.ajax({
    url        : 'http://192.168.1.22:5000/login',
    dataType   : 'json',
    contentType: 'application/json; charset=UTF-8', // This is the money shot
    data       : data,
    type       : 'POST',
    failure: function(errMsg) {
            alert(errMsg);
        }
    }).done(function(response) {
        alert(response);
      });
};
