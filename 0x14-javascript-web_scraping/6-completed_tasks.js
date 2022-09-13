#!/usr/bin/node
// number of tasks completed by user id

const axios = require('axios').default;
let ids;
// Make a request for a user with a given ID
const getid = async () => {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/users');
    ids = response.data.map(obj => {
      return obj.id;
    });
  } catch (error) {
    console.log(error);
  }
  axios.get(process.argv[2])
    .then(function (response) {
    // handle success
      const dict = {};
      for (let i = 0; i < ids.length; i++) {
        let count = 0;
        for (let idx = 0; idx < response.data.length; idx++) {
          if (response.data[idx].userId === ids[i] && response.data[idx].completed === true) {
            count += 1;
            dict[ids[i]] = count;
          }
        }
      }
      console.log(dict);
    })
    .catch(function (error) {
    // handle error
      console.log(error);
    });
};
getid();
