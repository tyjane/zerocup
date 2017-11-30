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
