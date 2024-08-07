$(document).ready(function () {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(apiUrl, function (data) {
    const helloTranslation = data.hello;
    $('#hello').text(helloTranslation);
  });
});
