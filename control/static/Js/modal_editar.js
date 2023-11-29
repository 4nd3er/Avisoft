var $ = jQuery.noConflict();
const abrirModalCrear = (url) => {
    $('#crear').load(url, function () {
        $(this).modal('show');
    });
};

const cerrarModalCrear = () => {
    $('#crear').modal('hide');
};

const abrirModalEditar = (url) => {
    $('#editar').load(url, function () {
        $(this).modal('show');
    });
};

const cerrarModalEditar = () => {
    $('#editar').modal('hide');
};

const abrirModalEliminar = (url) => {
    $('#eliminar').load(url, function () {
        $(this).modal('show');
    });
};

const cerrarModalEliminar = () => {
    $('#editar').modal('hide');
};

const registrar = () => {
    $.ajax({
        data: $('#formCreacion').serialize(),
        url: $('#formCreacion').attr('action'),
        type: $('#formCreacion').attr('method'),
        success: function (response) {
            console.log(response);
        },
        error: function (error) {
            console.log(error);
        }
    })
};