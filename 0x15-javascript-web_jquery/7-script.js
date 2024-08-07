$(document).ready(function () {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(apiUrl, function (data) {
    const characterName = data.name;
    $('#character').text(characterName);
  });
});
