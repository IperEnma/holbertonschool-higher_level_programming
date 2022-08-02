#!/usr/bin/node
// number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  list.forEach(element => {
    if (element === searchElement) { count++; }
  });
  return (count);
};
