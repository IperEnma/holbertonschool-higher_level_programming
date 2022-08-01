#!/usr/bin/node
// computes and prints a factorial

let number = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 1) { return (1); }
  return (number * factorial(number - 1));
}
if (Number.isInteger(number) && number > 0) {
  console.log(factorial(number));
} else {
  console.log(1);
}
