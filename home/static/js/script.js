(function () {
    var menu = document.querySelector('header div');
    var botao = document.getElementById('login');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) menu.classList.add('menuFixo');
        else menu.classList.remove('menuFixo');
        if (window.scrollY > 0) botao.classList.add('botaoFixo');
        else botao.classList.remove('botaoFixo');
    });
})();


let janelinhaLateral = document.querySelector("header div nav");
let menuHamburguer = document.querySelector(".menuHamburguer");

function abrirMenu(){
  janelinhaLateral.classList.toggle("abrirMenu");
}

menuHamburguer.onclick = abrirMenu;