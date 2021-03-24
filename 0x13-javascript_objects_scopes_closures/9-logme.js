#!/usr/bin/node
let flag = 0;
exports.logMe = function (item) {
  console.log(`${flag}` + ': ' + `${item}`);
  flag++;
};
