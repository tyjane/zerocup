var stories = document.getElementsByName('story')
for (var i = 0; i < stories.length; i++) {
    story = stories[i].innerHTML
    var newstory = ''
    for (var j = 0; j < story.length; j++) {
        if (story.charAt(j) == '\n') {
            newstory += '<br>'
        } else {
            newstory += story.charAt(j)
        }
    }
    document.getElementsByName('story')[i].innerHTML = newstory
}
