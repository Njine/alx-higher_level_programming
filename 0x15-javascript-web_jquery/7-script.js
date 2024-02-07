/* global $ */

$(document).ready(function () {
  $.getJSON('https://swapi.co/api/people/5/?format=json', function (characters) {
    $('#character').text(characters.name);
  });
});
