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
    const query = () => {
        const galpon = $('#id_galpon').val();
        $.ajax({
            url: `/galponDataDes/${galpon}`,
            method: 'GET',
            success: function (response) {
                responseGall = response.cant_gall;
                opSaldo();
            },
            error: function (error) {
                console.log(error);
            }
        })
    }
    query();
}

function opSaldo() {
    let cantMuertas = Number($('#cant_muertas').val()) || 0;
    let cantDesc = Number($('#cant_descarte').val()) || 0;
    let nuevoSaldo = responseGall - (cantMuertas + cantDesc);
    saldo.val(nuevoSaldo);
}