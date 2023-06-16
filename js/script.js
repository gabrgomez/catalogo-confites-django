$(document).ready(function() {
    // Configuración del carrusel
    $('.carousel').carousel({
      interval: 3000, // Cambiar imagen cada 3 segundos
      pause: 'hover' // Pausar al pasar el mouse sobre el carrusel
    });
  
    // Agregar clase 'active' al primer elemento de la lista
    $('.carousel-indicators li:first').addClass('active');
    $('.carousel-item:first').addClass('active');
  });
  