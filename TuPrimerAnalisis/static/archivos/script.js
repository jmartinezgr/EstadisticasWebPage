let text = document.getElementById('text');
let botones = document.getElementById('home_buttons')
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill2 = document.getElementById('hill2');
let hill3 = document.getElementById('hill3');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');

window.addEventListener('scroll',() => {
    let value = window.scrollY;
    text.style.marginTop = value * 2 + 'px';
    botones.style.marginTop = 140 + (value * 2 ) + 'px'; 
    leaf.style.top = value * -1.5 + 'px';
    leaf.style.left = value * 1.5 + 'px';
    hill5.style.left = value * 1.5 + 'px';
    hill4.style.left = value * -1.5 + 'px'; 
    hill1.style.top = value * 0.8 + 'px';
});