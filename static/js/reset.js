
$("#btn3").click(function (f) {
    let username = $("#username").val();
    let password = $("#password").val();
    let pwd_reset_info = {
        username: username,
        password: password
    }
    s = JSON.stringify(pwd_reset_info);
    document.forms[0].reset();

    $.ajax({
        url:"/forgot_password",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(s)});

    e.preventDefault();
})