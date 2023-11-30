function stateFicha() {
    var selectState = document.getElementById('select_estado_ficha').options[document.getElementById('select_estado_ficha').selectedIndex].text;
    var state = document.getElementById('estado_ficha');

    if (selectState == 'Activo') {
        state.checked = true;
        state.value = '1';
    }
    if (selectState == 'Inactivo') {
        state.checked = false;
        state.value = '0';

    }
}