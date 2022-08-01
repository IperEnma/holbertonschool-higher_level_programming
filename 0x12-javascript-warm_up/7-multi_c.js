#!/usr/bin/node
// script that prints x times "C is fun"

let integer = parseInt(process.argv[2]);

if (Number.isInteger(integer)) {
  while (integer > 0) {
    console.log('C is fun');
    integer--;
  }
} else {
  console.log('Missing number of occurrences');
}
