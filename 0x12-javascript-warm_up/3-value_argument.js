#!/usr/bin/node
// prints the first argument

let count = 0;
for (count = 0; process.argv[count]; count++) {
  continue;
}
if (count > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
