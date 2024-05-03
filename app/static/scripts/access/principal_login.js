const imagen1 = "/static/images/formulario-imagen.webp"
const imagen2 = "/static/images/formulario-imagen2.webp"
const imagen3 = "/static/images/formulario-imagen3.webp"

// se establece un contador de imagen
let imagenActual = 1

const imagen = document.querySelector("#imagen-formulario")

// se repite el intervalo de cambiar de imagen cada 4 segundos
setInterval(() => {

  if (imagenActual === 1) {
    imagen.classList.add("oculto") // la imagen1 será transparente
    setTimeout(() => {
      imagen.setAttribute("src", imagen2) // cambia de imagen después de que se desvanece la imagen 1
      imagen.classList.remove("oculto") // remueve la clase oculto para hacer visible la imagen 2
    }, 800) // espera 800ms antes de cambiar la imagen
    // la imagen actual pasa a ser la imagen2
    imagenActual = 2
  } else if (imagenActual === 2) {
    imagen.classList.add("oculto") // la imagen2 será transparente
    setTimeout(() => {
      imagen.setAttribute("src", imagen3) // cambia de imagen después de que se desvanece la imagen2
      imagen.classList.remove("oculto") // remueve la clase oculto para hacer visible la imagen 1
    }, 800) // espera 800ms segundo antes de cambiar la imagen
    // la imagen actual pasa a ser la imagen1
    imagenActual = 3
  } else {
    imagen.classList.add("oculto"); // la imagen3 será transparente
    setTimeout(() => {
      imagen.setAttribute("src", imagen1) // cambia de imagen después de que se desvanece la imagen2
      imagen.classList.remove("oculto") // remueve la clase oculto para hacer visible la imagen 1
    }, 800); // espera 800ms segundo antes de cambiar la imagen
    // la imagen actual pasa a ser la imagen1
    imagenActual = 1;
  }
}, 4500)
