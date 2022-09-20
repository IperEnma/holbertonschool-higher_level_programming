$(document).ready(function () {
  $.ajax({
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    success: function (result) {
      $('DIV#hello').text(result.hello);
    }
  });
});
