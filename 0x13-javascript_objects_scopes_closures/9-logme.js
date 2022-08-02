#!/usr/bin/node
// prints the number of arguments

let index = 0;

exports.logMe = function (item) {
  console.log('%i: %s', index, item);
  index++;
};
