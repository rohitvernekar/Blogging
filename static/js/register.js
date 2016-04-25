function validatePassword(form) {
    var username = document.getElementById("id_username").value
    var password = document.getElementById("id_password")
    var repassword = document.getElementById("id_repassword")
    if (username.length <= 5) {
        document.getElementById("div_id_username").innerHTML="Username should atleast contain more than 5 character"
        form.username.focus()
    }
    if (password!=repassword) {
        form.password.focus()
        document.getElementById("div_id_password").innerHTML = '<span style="color:#FF0000"> Both password entered should be same </span>';
    }
}

/*function validateUserNameLength(){
    var username = document.getElementById("id_username")
    if (username.length) <= 5{
        alert("Username should atleast contain more than 5 character")
    }
}

function CheckRegistrationForm(this){

}*/
