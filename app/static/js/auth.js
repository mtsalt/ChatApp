// PORT
function postRequest(objData) {
    let postUrl = location.href;
    let jsonData = JSON.stringify(objData);

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // callback process
            console.log("post success.");
        }
    }

    xhr.open("POST", postUrl);
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8');
    xhr.withCredentials = true;
    xhr.send(jsonData);
}

// REGISTER
function getRegisterInfo() {
    let registerInfo = {
        user_id: document.getElementById("user_id").value,
        password: document.getElementById("password").value,
        confirm_password: document.getElementById("confirm_password").value,
        display_name: document.getElementById("display_name").value,
        search_id: document.getElementById("search_id").value
    };
    return registerInfo;
}

function execRegister() {
    let registerInfo = getRegisterInfo();
    postRequest(registerInfo);
}


// LOGIN
function getLoginInfo() {
    let loginInfo = {
        user_id: document.getElementById("user_id").value,
        password: document.getElementById("password").value
    };
    return loginInfo;
}

function execLogin() {
    let loginInfo = getLoginInfo();
    postRequest(loginInfo);
}


// LOGOUT
// need to get identification info to finish session.
function execLogout() {
    let logoutUrl = location.host;

}