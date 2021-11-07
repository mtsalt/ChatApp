const base_url = "http://172.17.0.2:8080";
// const base_url = "192.168.11.16:8080";

function send_button_click() {
    
    // get id & passwrod string
    let id = document.getElementById("id").value;
    let password = document.getElementById("password").value;
    
    // create json data
    let obj_for_json = {"id": id, "password": password};
    let json_str = JSON.stringify(obj_for_json);
    console.log(json_str);

    // post
    let res = post_json("/", json_str, callbackfunc_post_json);
}

function post_json(url, json_str, callbackfunc) {

    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            callbackfunc(xhr.responseText);
        }
    }

    xhr.open("POST", url)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8');
    xhr.withCredentials = true;
    xhr.send(json_str);
}

function callbackfunc_post_json(res) {

    if(res != "authentication error."){
        // page transition
        console.log(res);
        // window.location.href = "https://www.google.com/";
    }
    else{
        alert("パスワードが違います。");
    }
}