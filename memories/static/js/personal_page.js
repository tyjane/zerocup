var memories = document.getElementById('memories').childNodes
for (var i = 0; i < memories.length; i++) {
    if (i % 2 == 0) {
        continue;
    }
    if ((i + 1) % 4 == 0) {
        (memories[i].style).backgroundColor = 'white'
    } else {
        (memories[i].style).backgroundColor = 'grey'
    }
}
var intro = document.getElementById('intro').innerHTML
var newintro = ''
for (var j = 0; j < intro.length; j++) {
    if (intro.charAt(j) == '\n') {
        newintro += '<br>'
    } else {
        newintro += intro.charAt(j)
    }
}
document.getElementById('intro').innerHTML = newintro
