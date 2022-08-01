#!/usr/bin/node
// computes and prints a factorial

function factorial (number, mul) {
  if (mul == 1) { return (number); }
  return (mul * factorial(number, mul - 1));
}

const number = parseInt(process.argv[2]);

if (Number.isInteger(number) && number > 0) {
  console.log(factorial(number, number - 1));
} else {
  console.log(1);
}
