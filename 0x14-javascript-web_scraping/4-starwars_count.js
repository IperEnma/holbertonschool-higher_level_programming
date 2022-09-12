#!/usr/bin/node
// where the character “Wedge Antilles” is present.

const axios = require('axios').default;

// Make a request for a user with a given ID

const url = process.argv[2];
axios.get(url)
  .then(function (response) {
    let count = 0;
    for (let idx = 0; idx < response.data.results.length; idx++) {
      for (let idc = 0; idc < response.data.results[idx].characters.length; idc++) {
        if (response.data.results[idx].characters[idc].includes('18')) {
		  count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
