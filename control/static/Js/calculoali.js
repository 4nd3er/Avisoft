function calculoAlim() {
    gr_gallina = document.getElementById('gr_gallina_dia').value;
    kg_total = document.getElementById('kg_total');
    bultos_total = document.getElementById('bultos_total');
    c_a = document.getElementById('c_a');
    total1 = Number(gr_gallina) / 1000;
    resulatdo1 = Number(total1) * 609;
    round = resulatdo1;
    kg_total.value = Math.round(round);
    total2 = Number(gr_gallina) / 40;
    bultos_total.value = total2;
}