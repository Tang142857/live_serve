var mothed_input = document.getElementById("mnput");
var address_input = document.getElementById("lnput");
var show = document.getElementById("vshow");
var button = document.getElementById("f5");

// tang's default config
mothed_input.value = "GET";
address_input.value = "http://192.168.0.109:8080/";

var getAttr = function(obj) {
    resString = "";
    for (let key in obj) {
        keyInfoString = key + " -> " + obj[key];
        resString += keyInfoString
        resString += "<br>"
    }
    return resString
}

var buttonCallback = function() {
    var mothed = mothed_input.value;
    var address = address_input.value;
    var requests = new XMLHttpRequest;
    requests.open(mothed, address);
    requests.send();
    requests.onreadystatechange = function() {
        var returnString = getAttr(requests);
        show.innerHTML = returnString;
    }
}

button.onclick = buttonCallback;