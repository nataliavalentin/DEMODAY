let container = document.querySelector('.popup');
let fundo = document.querySelector('.fundoPopup');
let botao = document.querySelector('.botao');

let tecnologia = document.querySelector('#id_choices li:nth-child(1)');
let diversao = document.querySelector('#id_choices li:nth-child(2)');
let fotografia = document.querySelector('#id_choices li:nth-child(3)');
let gastronomia = document.querySelector('#id_choices li:nth-child(4)');
let bonsDrinks = document.querySelector('#id_choices li:nth-child(5)');
let musica = document.querySelector('#id_choices li:nth-child(6)');
let moda = document.querySelector('#id_choices li:nth-child(7)');
let viagem = document.querySelector('#id_choices li:nth-child(8)');

botao.onclick = fecharPopup;

function fecharPopup(){
    container.style.display = 'none';
    fundo.style.display = 'none';
}

tecnologia.style.background= 'url(/static/images/interesses/tecnologia.png)';
tecnologia.style.display= 'flex';
tecnologia.style.alignItems= 'center';
tecnologia.style.justifyContent= 'center';
tecnologia.style.backgroundSize = 'cover';

diversao.style.background= 'url(/static/images/interesses/diversao.png)';
diversao.style.backgroundSize = ' cover';
diversao.style.display= 'flex';
diversao.style.alignItems= 'center';
diversao.style.justifyContent= 'center';

fotografia.style.background= 'url(/static/images/interesses/fotografia.png)';
fotografia.style.backgroundSize = ' cover';
fotografia.style.display= 'flex';
fotografia.style.alignItems= 'center';
fotografia.style.justifyContent= 'center';

gastronomia.style.background= 'url(/static/images/interesses/gastronomia.png)';
gastronomia.style.backgroundSize = ' cover';
gastronomia.style.display= 'flex';
gastronomia.style.alignItems= 'center';
gastronomia.style.justifyContent= 'center';

bonsDrinks.style.background= 'url(/static/images/interesses/bonsDrinks.png)';
bonsDrinks.style.backgroundSize = ' cover';
bonsDrinks.style.display= 'flex';
bonsDrinks.style.alignItems= 'center';
bonsDrinks.style.justifyContent= 'center';

musica.style.background= 'url(/static/images/interesses/musica.png)';
musica.style.backgroundSize = ' cover';
musica.style.display= 'flex';
musica.style.alignItems= 'center';
musica.style.justifyContent= 'center';

moda.style.background= 'url(/static/images/interesses/moda.png)';
moda.style.backgroundSize = ' cover';
moda.style.display= 'flex';
moda.style.alignItems= 'center';
moda.style.justifyContent= 'center';

viagem.style.background= 'url(/static/images/interesses/viagem.png)';
viagem.style.backgroundSize = ' cover';
viagem.style.display= 'flex';
viagem.style.alignItems= 'center';
viagem.style.justifyContent= 'center';