let botao = document.querySelector(".menu");
let uls = document.querySelector("ul");
botao.onclick = menuResponsivo;

function menuResponsivo() {
    uls.classList.toggle("mostrarUl");
}