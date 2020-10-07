function send_ajax(url, method, params){

    var xhttp = new XMLHttpRequest();
    xhttp.open(method, url);
    xhttp.setRequestHeader("Content-type", "application/json");
    console.log(params);
    xhttp.send(JSON.stringify(params));

}