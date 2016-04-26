function validatePassword(form) {
    var username = document.getElementById("id_username").value
    var email = document.getElementById("id_email")
    var password = document.getElementById("id_password")
    var repassword = document.getElementById("id_repassword")
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (username.length <= 5) {
        document.getElementById("div_id_username").innerHTML="Username should atleast contain more than 5 character"
        form.username.focus()
        return false
    }
    else{
        document.getElementById("div_id_username").innerHTML=""
    }
    if (password.value!=repassword.value) {
        document.getElementById("div_id_password").innerHTML = '<span style="color:#FF0000"> Both password entered should be same </span>';
        form.password.focus()
        return false
    }
    else {
        document.getElementById("div_id_password").innerHTML = ''
    }
    return true
}

/*function validateUserNameLength(){
    var username = document.getElementById("id_username")
    if (username.length) <= 5{
        alert("Username should atleast contain more than 5 character")
    }
}

function CheckRegistrationForm(this){

}*/
