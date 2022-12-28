var back = document.getElementById('main-block');
var position = 1;
var formula = ''

function minus () {
    if (position <2) {
        position = 22;
    }

    position = position -1;
    formula = 'url(Картинка-' + position + '.jpg)';
    back.style.backgroundImage = formula 
}

function plus() {
    if (position >21) {
        position = 0;
    }

    position = position + 1;
    formula = 'url(Картинка-' + position + '.jpg)';
    back.style.backgroundImage = formula
}
function Slaid(url) {
    back.style.backgroundImage = 'url(' + url + ')';
}