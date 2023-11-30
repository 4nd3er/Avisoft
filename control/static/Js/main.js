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

const registrar = () => {
    $.ajax({
        data: $('#formCreacion').serialize(),
        url: $('#formCreacion').attr('action'),
        type: $('#formCreacion').attr('method'),
        success: function (response) {
            console.log(response);
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
        data: $('#formEdicion').serialize(),
        url: $('#formEdicion').attr('action'),
        type: $('#formEdicion').attr('method'),
        success: function (response) {
            console.log(response);
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

const mostrarErroresCrear = (errores) => {
    $('#errores').html("");
    let error = "";
    for (let i in errores.responseJSON.error) {
        error += '<div class="alert alert-danger"><strong>' + errores.responseJSON.error[i] + '</strong></div>'
    }
    $('#errores').append(error);
}

const mostrarErroresEditar = (errores) => {
    $('#erroresEditar').html("");
    let error = "";
    for (let i in errores.responseJSON.error) {
        error += '<div class="alert alert-danger"><strong>' + errores.responseJSON.error[i] + '</strong></div>'
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
        timer: 1500,
        timerProgressBar: true,
    })
}