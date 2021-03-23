#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      result++;
    }
  }
  return (result);
};
