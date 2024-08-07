$(document).ready(function() {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const url = apiUrl + '?lang=' + languageCode;

    $.getJSON(url, function(data) {
      const helloTranslation = data.hello;
      $('#hello').text(helloTranslation);
    }).fail(function() {
      $('#hello').text('Error: Unable to fetch translation');
    });
  }

  $('language_code').click(function() {
    fetchTranslation();
  });

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
})
