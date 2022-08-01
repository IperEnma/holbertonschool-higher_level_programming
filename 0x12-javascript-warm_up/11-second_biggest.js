#!/usr/bin/node
// searches the second biggest

let max = 0;
let max2 = 0;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      max = parseInt(process.argv[i]);
    }
  }
  for (i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max2 && parseInt(process.argv[i]) !== max) {
      max2 = parseInt(process.argv[i]);
    }
  }
}
if (Number.isInteger(max2)) {
  console.log(max2);
} else {
  console.log(max);
}
