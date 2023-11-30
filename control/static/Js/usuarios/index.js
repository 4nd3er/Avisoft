
const listarDatosUsuario = () => {
    $.ajax({
        url: "/usuarios/",
        type: "get",
        dataType: "json",
        success: function (response) {
            console.log(response);
        },
        error: function (error) {
            console.log(error);
        }
    })
};