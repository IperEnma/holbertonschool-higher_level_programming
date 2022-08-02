#!/usr/bin/node
// reversed version of a list

exports.esrever = function (list) {
  for (i = 0, j = list.length - 1; i < j; i++, j--) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return (list);
};
