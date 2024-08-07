$(document).ready(function () {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(apiUrl, function (data) {
    const movies = data.results;
    $.each(movies, function (index, movie) {
      const listItem = $('<li></li>').text(movie.title);
      $('#list_movies').append(listItem);
    });
  });
});
