function stateFicha() {
    const selectState = document.getElementById('select_estado_ficha').options[document.getElementById('select_estado_ficha').selectedIndex].value;
    const state = document.getElementById('estado_ficha');

    state.value = selectState;
}