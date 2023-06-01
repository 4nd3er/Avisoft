function calcuateArea() {
ancho = document.getElementById('ancho').value;
largo = document.getElementById('largo').value;
area = document.getElementById('area');
    resultado = ancho * largo;
    area.value = resultado
};

function calculateAves(){
    area = document.getElementById('area').value;
    capac_gall = document.getElementById('capac_gall');
    taves = area * 8;
    capac_gall.value = taves


};