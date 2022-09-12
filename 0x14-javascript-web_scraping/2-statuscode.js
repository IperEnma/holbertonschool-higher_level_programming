#!/usr/bin/node
// write text in file

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    console.log(response.status);
  });
