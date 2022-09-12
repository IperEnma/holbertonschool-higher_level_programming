#!/usr/bin/node
// where the character “Wedge Antilles” is present.

const axios = require('axios').default;

// Make a request for a user with a given ID
axios.get('https://swapi-api.hbtn.io/api/people/18')
  .then(function (response) {
    console.log(response.data.films.length);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
