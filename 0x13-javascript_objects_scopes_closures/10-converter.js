#!/usr/bin/node
// 10 to another base passed as argument

let baseG;

function myConverser (num) {
  const result = num.toString(baseG);
  return (result);
}

exports.converter = function (base) {
  baseG = base;
  return (myConverser);
};
