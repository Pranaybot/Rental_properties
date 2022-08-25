
$("#btn").submit(function (f) {
    let username = $("#username").val();
    let password = $("#password").val();

    $.ajax({
        url:"/",
        type: "POST",
        data:{'Username':username,
        'Password':password}
    });

    e.preventDefault();
})

