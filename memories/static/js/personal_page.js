var log = function() {
     console.log.bind(console)
}
var memories = document.getElementById('memories').childNodes
log("memories", memories)
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
// log("memories", memories)
var intro = document.getElementById('intro').innerHTML
// log("intro", intro)
var newIntro = ''
for (var j = 0; j < intro.length; j++) {
    if (intro.charAt(j) == '\n') {
        newIntro += '<br>'
    } else {
        newIntro += intro.charAt(j)
    }
}
document.getElementById('intro').innerHTML = newIntro

canvas = document.getElementById("canvas")
context = canvas.getContext("2d")

img = new Image()
img.src = "/static/css/images/calendar.png"
context.drawImage(img, 0, 0)
