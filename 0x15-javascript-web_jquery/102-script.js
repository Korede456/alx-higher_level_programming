$(document).ready(funciton() {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();

    const url = apiUrl + '?lang=' + languageCode;
    $.getJSON(url, funciton(data) {
      const helloTranslation = data.hello;
      $('#hello').text(helloTranslation);
    }).fail(function() {
      $('#hello').text('Error: Unable to fetch translation');
    });
  });
});
