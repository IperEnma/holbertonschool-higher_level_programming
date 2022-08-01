#!/usr/bin/node
// prints a square

const integer = parseInt(process.argv[2]);

if (Number.isInteger(integer)) {
  for (let i = 0; i < integer; i++) {
    console.log('x'.repeat(integer));
  }
} else {
  console.log('Missing size');
}
