let container = document.querySelector('.popup');
let fundo = document.querySelector('.fundoPopup');
let botao = document.querySelector('.botao');

botao.onclick = fecharPopup;

function fecharPopup(){
    container.style.display = 'none';
    fundo.style.display = 'none';
}
