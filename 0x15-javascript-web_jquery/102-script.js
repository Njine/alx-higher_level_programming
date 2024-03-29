/* global $ */

$(document).ready(function () {
  $('#btn_search').click(function () {
    const city = $('#city_search').val();
    const apiUrl = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json';

    $.get(apiUrl, function (data, status) {
      if (status === 'success' && data.query.results.channel) {
        $('#wind_speed').text(data.query.results.channel.wind.speed);
      }
    });
  });
});
