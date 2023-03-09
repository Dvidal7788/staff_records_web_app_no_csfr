function togglePasswordText() {
    var x = document.getElementById("passwordInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }


function togglePasswordConfirmationText() {
    var x = document.getElementById("passwordConfirmationInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }


// function togglePasswordConfirmationText() {
//     var x = document.querySelector(".pass");
//     for (i in x) {
//       if (type[i] === "password") {
//         type[i] = "text";
//       } else {
//         type[i] = "password";
//       }
//     }

//   }