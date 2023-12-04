//Galpon actual
const selectGalpon = document.querySelector(".selectGalpon");
//Id galpon seleccionado
const idGalpon = document.getElementById("idGalpon")
//Galpones
const Galpones = document.querySelectorAll(".galpon")
let cantGall = 0;

//Cada que cambie de galpon
selectGalpon.addEventListener("change", function () {

    //Idgalpon es igual al valor del galpon seleccionado
    idGalpon.value = selectGalpon.value

    //Para cada galpon comparar el idgalpon
    Galpones.forEach(function (galpon) {
        const dataId = galpon.getAttribute("data-id");

        //Traer la cant_gall del data-id que coincida con idgalpon
        if (dataId == idGalpon.value) {
            cantGall = parseFloat(galpon.value) || 0;
        }
    });

});

//Calcular saldo
const cantMuertas = document.querySelector(".cant_muertas");
const cantDesc = document.querySelector(".cant_descarte");
const Saldo = document.getElementById("saldo");

function actualizarSuma() {
    var valor1 = parseFloat(cantMuertas.value) || 0;
    var valor2 = parseFloat(cantDesc.value) || 0;
    var suma = parseFloat(cantGall) - (valor1 + valor2)
    if (valor1 > 0 && valor2 > 0) {
        Saldo.value = suma
    }
}

//Cada que escriba algo el saldo se actualiza
cantMuertas.addEventListener("input", actualizarSuma);
cantDesc.addEventListener("input", actualizarSuma)

//Actualizar saldo