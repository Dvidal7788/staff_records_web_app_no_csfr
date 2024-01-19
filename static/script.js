
function togglePasswordConfirmationText() {
  console.log(document.querySelector('.password-input'));
  const passwordInputs = document.querySelectorAll('.password-input');

  for (let input of passwordInputs) {
    if (input.type === 'text') {
      input.type = 'password';
    } else {
      input.type = 'text';
    }
  }
}


document.addEventListener('DOMContentLoaded', () => {

  // Retrieve checkbox
  let checkbox = document.querySelector('#checkbox')

  // Reset checkbox if page is refreshed (autocomplete="off" in HTML also works for this)
  checkbox.checked = false;

  // Set onclick to function
  checkbox.onclick = togglePasswordConfirmationText;
});