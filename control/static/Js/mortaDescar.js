const selectGalpon = document.getElementById("id_galpon");
let saldo = $('#saldo');
let responseGall;

if (saldo.val() == '') {
    selectGalpon.addEventListener("input", function (e) {
        if (e.target.value != '') {
            $.ajax({
                url: `/galponDataDes/${e.target.value}`,
                method: 'GET',
                success: function (response) {
                    responseGall = response.cant_gall;
                    saldo.val(responseGall);
                },
                error: function (error) {
                    console.log(error);
                }
            })
        }
        else {
            $('#saldo').val('');
        }
    });
}
else {
    let cantMuertas = Number($('#cant_muertas').val()) || 0;
    let cantDesc = Number($('#cant_descarte').val()) || 0;
    responseGall = Number(saldo.val()) + (cantMuertas + cantDesc);
}

function opSaldo() {
    let cantMuertas = Number($('#cant_muertas').val()) || 0;
    let cantDesc = Number($('#cant_descarte').val()) || 0;
    let nuevoSaldo = responseGall - (cantMuertas + cantDesc);
    saldo.val(nuevoSaldo);
}