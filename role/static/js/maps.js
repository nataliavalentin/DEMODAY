let container = document.querySelector('#location-map');
let fundo = document.querySelector('.fundoPopup');
let popup = document.querySelector('.popup');
let botao = document.querySelector('.botao');
let voltar = document.querySelector('.voltar');

botao.onclick = abrirPopup;
voltar.onclick = fecharPopup;

function abrirPopup(){
    container.style.display = 'flex';
    popup.style.display = 'flex';
    fundo.style.display = 'flex';
}

function fecharPopup(){
    container.style.display = 'none';
    popup.style.display = 'none';
    fundo.style.display = 'none';
}

let map = L.map('location-map').setView([	-23.556647, -46.6586428], 17);
    mapLink = '<a href="https://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; ' + mapLink,
            maxZoom: 20,
        }).addTo(map);
    let marker = L.marker([-23.556647, -46.6586428]).addTo(map);