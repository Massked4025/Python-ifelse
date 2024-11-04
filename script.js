function validate(e){
    e.preventDefault();

    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgbox = document.getElementById("message");

    let message = "";

    if(email===""){
        message="email is required";
        msgbox.style.color="red";
    } else if(pass===""){
        message="password is required";
        msgbox.style.color="red";
    } else if(age===""){
        message="age is required";
        msgbox.style.color="red";
    } else {
        message="Login succesful";
        msgbox.style.color="green";
    }
    msgbox.innerText = message
}