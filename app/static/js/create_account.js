function create_account_button_click() {
    
    let id = document.getElementById("id-str").value;
    let display_name = document.getElementById("displayname-str").value;
    let password = document.getElementById("password-str").value;
    let search_id = document.getElementById("searchid-str").value;

    if(id != "" && display_name != "" && password != "" && search_id != "") {
        let json_obj = {
            "id" : id,
            "display_name" : display_name,
            "password" : password,
            "search_id" : search_id
        }
        let json_str = JSON.stringify(json_obj);

        // post
        let res = post_json("/account", json_str, callbackfunc_post_json);
    }
    else {
        alert("すべての項目を入力してください。");
    }
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