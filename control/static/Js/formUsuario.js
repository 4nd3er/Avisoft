function AdminUser() {
    let rol_value = document.getElementById('id_rol').options[document.getElementById('id_rol').selectedIndex].text;
    let admin = document.getElementById('is_staff');

    if (rol_value == 'Administrador') {
        admin.checked = true;
        admin.value = 'true';
    }
    if (rol_value == 'Aprendiz') {
        admin.checked = false;
        admin.value = 'false';

    }
}