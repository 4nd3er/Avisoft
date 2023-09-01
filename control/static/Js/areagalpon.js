function calcuateArea() {
    let ancho = document.getElementById('ancho').value || 0;
    let largo = document.getElementById('largo').value || 0;
    let area = document.getElementById('area');
    let capac_gall = document.getElementById('capac_gall');
    let capac_bebed = document.getElementById('capac_bebed');
    let capac_nidales = document.getElementById('capac_nidales');
    let capac_comed = document.getElementById('capac_comed');
    resultado = ancho * largo;
    area.value = resultado;
    resultado2 = resultado * 6;
    capac_gall.value = resultado2;
    resultado3 = resultado2 / 25;
    capac_bebed.value = Math.round(resultado3);
    resultado4 = resultado2 / 5;
    capac_nidales.value = Math.round(resultado4);
    capac_comed.value = Math.round(resultado3);
}; // ? Funcion para calcular el area y demas cosas en vivo

const onlyNumber = () => {
    return event.charCode >= 48 && event.charCode <= 57;
}; // ? Funcion que solo permite numeros en el input