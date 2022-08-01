#!/usr/bin/node
import { argv } from 'node:process';

// prints a message depending of args
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
