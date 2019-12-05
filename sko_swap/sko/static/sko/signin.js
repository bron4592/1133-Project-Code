function signin_verify(){
  var email = document.getElementById('inputEmail').vlaue;
  var password = document.getElementById('inputPassword').value;

  if(email == "test@test.com" && password == "test"){
    return window.location.href = "testHome.html";
  }
  else{
    alert("Incorrect email or password");
  }
}
