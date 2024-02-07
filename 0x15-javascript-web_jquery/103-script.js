$(document).ready(function() {
  $('#btn_translate').click(translate);
  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      translate();
    }
  });
});

function translate() {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  const languageCode = $('#language_code').val();
  
  $.get(url + languageCode, function(data) {
    $('#hello').text(data.hello);
  });
}
