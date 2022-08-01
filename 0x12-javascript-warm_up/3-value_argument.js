#!/usr/bin/node
// prints the first argument

import { argv } from 'node:process';
if (argv.length > 2) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
