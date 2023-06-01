function calcuateArea() {
ancho = document.getElementById('ancho').value;
largo = document.getElementById('largo').value;
area = document.getElementById('area');
capac_gall = document.getElementById('capac_gall');
capac_bebed = document.getElementById('capac_bebed');
capac_nidales = document.getElementById('capac_nidales');
capac_comed = document.getElementById('capac_comed');
    resultado = ancho * largo;
    area.value = resultado;
    resultado2 = resultado * 6;
    capac_gall.value = resultado2;
    resultado3 = resultado2 / 25;
    capac_bebed.value = Math.round(resultado3);
    resultado4 = resultado2 / 5;
    capac_nidales.value = Math.round(resultado4);
    capac_comed.value = Math.round(resultado3);

    
};