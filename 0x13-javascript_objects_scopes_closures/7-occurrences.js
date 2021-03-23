#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = '';
  for (const i in list) {
    if (list[i] === searchElement) {
      result++;
    }
  }
  return (result);
};
