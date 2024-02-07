/* global $ */

$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('text-red text-green');
  });
});
