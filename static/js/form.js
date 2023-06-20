$(document).ready(function() {
// Validación del formulario

$("#login-form").validate({
  rules: {
    firstname: "required",
      lastname1: "required",
      lastname2: "required",
    email: {
      required: true,
      email: true
    },
    password: {
      required: true,
      minlength: 5
    }
  },
  //fin de las reglas
  messages: {
    firstname: "Por favor, introduzca su nombre",
      lastname1: "Por favor, introduzca su primer apellido",
      lastname2: "Por favor, introduzca su segundo apellido",
    email: {
      required: "Por favor, introduzca su dirección de correo electrónico",
      email: "Por favor, introduzca una dirección de correo electrónico válida"
    },
    password: {
      required: "Por favor, introduzca su contraseña",
      minlength: "La contraseña debe tener al menos 5 caracteres"
    }
  },
  //fin de los mensajes
  
  




})
//fin del validate
$("#btnRegistro").click(function (event) {

  
  

  //   esto es para que no direccione
    event.preventDefault();
    
    if ($("#login-form").valid()) {
      alert("¡registrado con exito! =D");


}


})
//fin del on click
});
//fin de doc ready
