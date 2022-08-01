#!/usr/bin/node
// prints the first argument

import { argv } from 'node:process';
let count = 0;
for (count = 0; argv[count]; count++) {
}
if (count > 2) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
