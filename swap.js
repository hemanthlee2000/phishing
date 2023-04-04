// Check if the current website is a phishing website
if (isPhishingWebsite()) {
  // Get the form element
  var form = document.getElementsByTagName('form')[0];

  // Get the input fields in the form
  var inputs = form.getElementsByTagName('input');

  // Loop through the input fields and replace their values
  for (var i = 0; i < inputs.length; i++) {
    inputs[i].value = "Fake Value";
  }
  
  // Disable the submit button
  var submitButton = form.querySelector('input[type="submit"]');
  submitButton.disabled = true;

  // Add an event listener to the form to prevent it from being submitted
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('This website is a phishing site!');
  });
}

function isPhishingWebsite() {
  // Logic to determine if the current website is a phishing website
  // This could include comparing the URL against a list of known phishing sites, or using machine learning to analyze the page content
  // For demo purposes, we'll assume that any website with the word "phishing" in the URL is a phishing site
  var url = window.location.href;
  return url.includes('phishing');
}
