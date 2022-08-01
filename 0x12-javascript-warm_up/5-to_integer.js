#!/usr/bin/node
// converted to an integer

import { argv } from 'node:process';

const integer = parseInt(argv[2], 10);
if (Number.isInteger(integer)) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
