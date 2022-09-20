$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (result) {
      for (let i = 0; i < result.results.length; i++) {
	  	$('UL#list_movies').append('<li>' + result.results[i].title + '</li>');
	  }
    }
  });
});
