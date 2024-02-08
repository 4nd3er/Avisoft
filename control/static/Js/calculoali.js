let gr_gallina_data = '';
function galponDataForm() {
    let galponSelect = document.getElementById('id_galpon');

    galponSelect.addEventListener('change', function (e) {
        let gr_gallina_dia = document.getElementById('gr_gallina_dia');
        let kg_total = document.getElementById('kg_total');
        let bultos_total = document.getElementById('bultos_total');
        let c_a = document.getElementById('c_a');
        if (e.target.value != '') {
            $.ajax({
                url: `/galponData/${e.target.value}`,
                method: 'GET',
                success: function (response) {
                    gr_gallina_data = response.dataGalpon.cant_gall;
                    function calculoAlim() {
                        gr_gallina_dia.value = gr_gallina_data * 110;
                        total1 = Number(gr_gallina_data) / 1000;
                        resultado1 = (Number(total1) * 609).toFixed(2);
                        kg_total.value = resultado1;
                        total2 = (Number(gr_gallina_data) / 40).toFixed(2);
                        bultos_total.value = total2;
                        c_a.value = 0;                        
                        if (response.dataProd !== 0) c_a.value = (resultado1 / (Number(response.dataProd) / 12)).toFixed(2);
                    }
                    calculoAlim();
                },
                error: function (error) {
                    console.log(error);
                }
            })
        }
        else {
            gr_gallina_dia.value = '';
            kg_total.value = '';
            bultos_total.value = '';
            c_a.value = '';
        }
    })
    
}