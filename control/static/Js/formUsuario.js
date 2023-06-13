function AdminUser() {
    var rol_value = document.getElementById('id_rol').options[document.getElementById('id_rol').selectedIndex].text;
    var admin = document.getElementById('is_staff');

    if (rol_value == 'Administrador') {
        admin.checked = true;
    }
    if (rol_value == 'Aprendiz') {
        admin.checked = false;

    }
}