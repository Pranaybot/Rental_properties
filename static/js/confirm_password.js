
function register() {

    var password= document.getElementById('password').value ;
    var confirm= document.getElementById('confpassword').value;

    if (password!=confirm){
      var field = document.getElementById("checkconfirm")
      field.innerHTML = "not match";
    }
    else {
      var field = document.getElementById("checkconfirm")
      field.innerHTML = "Passwords match";
    }
  }