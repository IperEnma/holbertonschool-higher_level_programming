#!/usr/bin/node
// gets the contents of a webpage

const axios = require('axios').default;
const fs = require('fs');
// Make a request for a user with a given ID
axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    fs.writeFile(process.argv[3], response.data, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
