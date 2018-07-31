// Write your Javascript code.

function showNavDrop(ev) {
    //shows the drop down description for each link
    var target = $(ev.target);
    var elemText = target.text;
    var dropPara = document.getElementById("navdropdown")
    //dropPara.style.display = 'block';
    switch (elemText) {
        default:
            dropPara.textContent =  "Default";
        case "Bio":
            dropPara.textContent = "Bio Show";
            break;
        case "":
            break;
    }
}

function hideNavDrop(ev) {
    var dropPara = document.getElementById("navdropdown")
    //dropPara.style.display = 'none';
}