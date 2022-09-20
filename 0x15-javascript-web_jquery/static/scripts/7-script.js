$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (result) {
      $('DIV#character').text(result.name);
    }
  });
});
