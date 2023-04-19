/**
* PHP Email Form Validation - v3.6
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

  let forms = document.querySelectorAll('.django-email-form');

  forms.forEach(function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;
      let action = thisForm.getAttribute('action');

      if (!action) {
        displayError(thisForm, 'The form action property is not set!');
        return;
      }

      let formData = new FormData(thisForm);

      // Validate the form using Django's built-in form validation mechanisms
      fetch(action, {
        method: 'POST',
        body: formData,
        headers: {'X-Requested-With': 'XMLHttpRequest'}
      })
      .then(response => response.json())
      .then(data => {
        if (data['success']) {
          thisForm.querySelector('.sent-message').classList.add('d-block');
          thisForm.reset();
        } else {
          let errors = data['errors'];
          for (let field in errors) {
            let errorMessages = errors[field].join(' ');
            let fieldElem = thisForm.querySelector(`[name="${field}"]`);
            let errorElem = document.createElement('span');
            errorElem.className = 'text-danger';
            errorElem.textContent = errorMessages;
            fieldElem.parentNode.insertBefore(errorElem, fieldElem.nextSibling);
          }
        }
      })
      .catch(error => {
        displayError(thisForm, error);
      });
    });
  });

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();
