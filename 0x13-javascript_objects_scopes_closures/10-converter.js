#!/usr/bin/node
// 10 to another base passed as argument

exports.converter = function (base) {
  return function myConverser (num) {
    return num.toString(base);
  };
};
