function getLoginInfo() {
    let userId = document.getElementById("user_id").value;
    let password = document.getElementById("password").value;
    let loginInfo = {
        user_id: userId,
        password: password
    };
    return loginInfo;
}

function postLoginInfo() {

    let postUrl = location.href;
    let loginInfoJSON = JSON.stringify(getLoginInfo());

}