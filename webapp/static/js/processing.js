function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Appelle la fonction callback en lui passant la réponse de la requête
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    if (isJson) {
        // Définit le contenu de la requête comme étant du JSON
        req.setRequestHeader("Content-Type", "application/json");
        // Transforme la donnée du format JSON vers le format texte avant l'envoi
        data = JSON.stringify(data);
    }
    req.send(data);
}

function initMap(lat, lng) {
    var location = new google.maps.LatLng(lat, lng);
    var mapCanvas = document.querySelector(".map:last-of-type");
    var mapOptions = {
        center: location,
        zoom: 16,
        panControl: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    var map = new google.maps.Map(mapCanvas, mapOptions);

}

var form = document.querySelector("#formReq");

form.addEventListener("submit", function (e) {
    e.preventDefault();
    let data = new FormData(formReq);
    ajaxPost("ajax", data, function (response) {
        let data = JSON.parse(response);
        var repGpy = document.createElement("li"); 
        repGpy.id = "repGpy";
        repGpy.appendChild(document.createTextNode(data["commentary"])); 
        document.getElementById("answer").appendChild(repGpy);
        
        // Adding address infos
        if (data["result"]>=1) {
            var address = document.createElement("li"); 
            address.id = "address"; 
            address.appendChild(document.createTextNode("Ce lieu se situe à cette adresse : "+ data["adress"])); 
            document.getElementById("answer").appendChild(address);

            // creating a new var
            var gmap = document.createElement("li");
            gmap.className = "map";
            document.getElementById("answer").appendChild(gmap);

            initMap(data["latitude"], data["longitude"]);
            
        }

        // Adding wiki infos and url
        if (data["result"]===2) {
            // adding summary
            var wikiInfo = document.createElement("li");
            wikiInfo.id = "wikiInf";
            wikiInfo.appendChild(document.createTextNode(data["summary"]));
            document.getElementById("answer").appendChild(wikiInfo);
            

            // adding url of wikipedia
            var wikiLink = document.createElement("a");
            wikiLink.id = "urlWiki";
            wikiLink.href = data["link_wiki"]
            wikiLink.appendChild(document.createTextNode("Voici un lien vers Wikipédia"));
            document.getElementById("answer").appendChild(wikiLink);
        }
        let element = document.querySelector("section li:last-of-type");
        element.scrollIntoView();
    })
});
