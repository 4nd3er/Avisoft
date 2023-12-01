let $ = jQuery.noConflict();

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

// ----------------------------AJAX------------------------------------
const registrar = () => {
    $.ajax({
        data: $('#formCreacion').serialize(),
        url: $('#formCreacion').attr('action'),
        type: $('#formCreacion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(() => {
                cerrarModalCrear();
                window.location.reload();
            }, 1100);
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
        data: $('#formEdicion').serialize(),
        url: $('#formEdicion').attr('action'),
        type: $('#formEdicion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(() => {
                cerrarModalEditar();
                window.location.reload();
            }, 1100);
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
    $('#erroresEditar').append(error);
}

function notificacionError(mensaje) {
    Swal.fire({
        icon: 'error',
        title: 'Error!',
        text: mensaje,
        confirmButtonColor: "#C00",
    })
}

function notificacionSuccess(mensaje) {
    Swal.fire({
        icon: 'success',
        title: 'Usuario Registrado!',
        text: mensaje,
        timer: 1000,
        timerProgressBar: true,
    })
}