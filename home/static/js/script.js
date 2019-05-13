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

let logoNav = document.querySelector("header div a img");
let janelinhaLateral = document.querySelectorAll("header div nav ul");
let menuHamburguer = document.querySelector(".menuHamburguer");

function abrirMenu(){
  for (x of janelinhaLateral) {
    x.classList.toggle("aparecerBotao");
  }
  logoNav.classList.toggle("logoNav");
}

menuHamburguer.onclick = abrirMenu;