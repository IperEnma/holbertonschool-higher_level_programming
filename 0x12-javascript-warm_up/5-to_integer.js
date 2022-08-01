#!/usr/bin/node
// converted to an integer

const integer = parseInt(process.argv[2], 10);
if (Number.isInteger(integer)) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
