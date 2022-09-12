#!/usr/bin/node
// prints the tile of a Star wars movie

const axios = require('axios').default;

url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios.get(url)
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error
    console.log(error.response.status);
  });
