#!/usr/bin/node
// prints two arguments passed

import { argv } from 'node:process';

console.log(argv[2] + ' is ' + argv[3]);
