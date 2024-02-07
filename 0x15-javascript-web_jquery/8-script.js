/* global $ */

$(document).ready(function () {
  $.get('https://swapi.co/api/films/?format=json', function (filmsData) {
    $.each(filmsData.results, function (index, film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  }, 'json');
});
