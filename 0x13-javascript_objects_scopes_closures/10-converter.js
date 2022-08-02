#!/usr/bin/node
// 10 to another base passed as argument

function myConverser (num) {
  const result = num.toString(baseG);
  return (result);
}

exports.converter = function (base) {
  return (myConverser(base));
};
