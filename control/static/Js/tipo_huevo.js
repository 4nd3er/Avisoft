function mostrarInput() {
  var inputs = document.querySelector('.CantidadHuevo');
  for (var i = 0; i < inputs.length; i++) {
    if (this.checked) {
      inputs[i].style.display = 'flex';
    } else {
      inputs[i].style.display = 'none';
    }
  }
}

var checkboxes = document.querySelector('.lista');
for (var i = 0; i < checkboxes.length; i++) {
  checkboxes[i].addEventListener('change', mostrarInput);
}