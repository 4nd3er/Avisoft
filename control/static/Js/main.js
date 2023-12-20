let $ = jQuery.noConflict();

const abrirModalCrear = (url) => {
    $('#crear').load(url, function () {
        $(this).modal('show');
    });
};

const cerrarModalCrear = () => {
    $('#crear').modal('hide');
    setTimeout(() => {
        window.location.reload();
    }, 100);
};

const abrirModalEditar = (url) => {
    $('#editar').load(url, function () {
        $(this).modal('show');
    });
};

const cerrarModalEditar = () => {
    $('#editar').modal('hide');
    setTimeout(() => {
        window.location.reload();
    }, 100);
};

const abrirModalEliminar = (url) => {
    $('#eliminar').load(url, function () {
        $(this).modal('show');
    });
};

const cerrarModalEliminar = () => {
    $('#editar').modal('hide');
    setTimeout(() => {
        window.location.reload();
    }, 100);
};

// ----------------------------AJAX------------------------------------

const registrar = () => {
    $.ajax({
        data: $('.formCrear').serialize(),
        url: $('.formCrear').attr('action'),
        type: $('.formCrear').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(() => {
                cerrarModalCrear();
                window.location.reload();
            }, 1600);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCrear(error);
            setTimeout(() => {
                mostrarErroresCrear('');
            }, 5000);
        }
    })
};

const editar = () => {
    $.ajax({
        data: $('.formEditar').serialize(),
        url: $('.formEditar').attr('action'),
        type: $('.formEditar').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(() => {
                cerrarModalEditar();
                window.location.reload();
            }, 1600);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEditar(error);
            setTimeout(() => {
                mostrarErroresEditar('');
            }, 5000);
        }
    })
};

const registrarProdDiaria = () => {
    $.ajax({
        data: $('#formCrearProdDiaria').serialize(),
        url: $('#formCrearProdDiaria').attr('action'),
        type: $('#formCrearProdDiaria').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            $('#id_tipo_huevo').val('');
            $('#cantidad').val('');
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCrear(error);
            setTimeout(() => {
                mostrarErroresCrear('');
            }, 5000);
        }
    })
};

const EditarProdDiaria = () => {
    $.ajax({
        data: $('#formEditarProdDiaria').serialize(),
        url: $('#formEditarProdDiaria').attr('action'),
        type: $('#formEditarProdDiaria').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(() => {
                cerrarModalEditar();
                window.location.reload();
            }, 1600);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCrear(error);
            setTimeout(() => {
                mostrarErroresCrear('');
            }, 5000);
        }
    })
};

const selectJornada = () => {
    if ($('#id_jornada').val() != '') {
        $('#rotos').val('');
        $('#descarte').val('');
    }
};

const mostrarErroresCrear = (errores) => {
    $('#errores').html("");
    let error = "";
    for (let item in errores.responseJSON.error) {
        error = '<div class="m-2" style="font-size: .75rem; width: auto; color: #dc3545"><strong>' + errores.responseJSON.error[item] + '</strong></div>'
        $(`#errores${item}`).html(error);
    }
}

const mostrarErroresEditar = (errores) => {
    $('#erroresEditar').html("");
    let error = "";
    for (let item in errores.responseJSON.error) {
        error = '<div class="m-2" style="font-size: .75rem; width: auto; color: #dc3545"><strong>' + errores.responseJSON.error[item] + '</strong></div>'
        $(`#errores${item}`).html(error);
    }
    $('#erroresEditar ').append(error);
}

function notificacionSuccess(mensaje) {
    Swal.fire({
        icon: 'success',
        title: 'Bien hecho!',
        text: mensaje,
        timer: 1500,
        timerProgressBar: true,
        showConfirmButton: false,
    })
}

function notificacionError(mensaje) {
    Swal.mixin({
        toast: true,
        timer: 1500,
        position: 'top-end',
        showConfirmButton: false,
        timerProgressBar: true,
    }).fire({
        icon: 'error',
        title: 'Error!',
        text: mensaje
    })
}