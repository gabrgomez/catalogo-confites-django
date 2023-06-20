$("#btncargar").click(function (event) {


event.preventDefault();

var dog=$("#txtdog").val();
var url = "https://dog.ceo/api/breed/" + dog + "/images/random";

console.log(dog);




    fetch(url)
        .then(response => response.json())
        .then(data =>
            {
            //var perro =data.message;
            var perro = ("<p><img src='"+data.message+"'>");


            
            //var $precio = data.serie[0].valor;


            // console.log($nombre_indicador)




                // para limpiar el contedor antes de desplegar
                $("#info").empty();
                $('#info')
                .append(perro + "<br>")
                
        
                //.append($precio)                    


            })
        .catch(error => console.error(error));


});


