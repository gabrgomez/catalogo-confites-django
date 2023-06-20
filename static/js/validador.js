
$(function () {
  // Cuando se envía el formulario
  $('#formulario').submit(function (event) {
    event.preventDefault(); // Prevenir el envío del formulario

    // Validar el nombre
    var nombre = $('#nombre').val().trim();
    if (nombre === '') {
      alert('Debe ingresar su nombre.');
      $('#nombre').focus();
      return false;
    }

    // Validar el correo
    var correo = $('#correo').val().trim();
    if (correo === '') {
      alert('Debe ingresar su correo electrónico.');
      $('#correo').focus();
      return false;
    } else if (!validarCorreo(correo)) {
      alert('El correo electrónico ingresado no es válido.');
      $('#correo').focus();
      return false;
    }

    // Validar el mensaje
    var mensaje = $('#mensaje').val().trim();
    if (mensaje === '') {
      alert('Debe ingresar un mensaje.');
      $('#mensaje').focus();
      return false;
    }

    // Si se pasan todas las validaciones, mostrar mensaje
  
    $("#boton").click(function (event) {

      event.preventDefault();
  
      alert("¡Mensaje Enviado!");
  
  });
  });

  // Función para validar el correo electrónico
  function validarCorreo(correo) {
    var expresion = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
    return expresion.test(correo);
  }

  
});
