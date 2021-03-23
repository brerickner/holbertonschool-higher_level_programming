#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  for (let i = list.length - 1; i > -1; i--) {
    arr.push(list[i]);
  }
  return (arr);
};
