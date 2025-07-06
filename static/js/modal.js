const modal = document.getElementById("modal");
const abrirBtn = document.getElementById("abrirModal");
const cerrarBtn = document.getElementById("cerrarModal");

abrirBtn.onclick = function () {
  modal.style.display = "block";
};

cerrarBtn.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (e) {
  if (e.target === modal) {
    modal.style.display = "none";
  }
};
