#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // parent class's constructor with size provided for the Rectangle's width and height
    super(size, size);
  }
}
module.exports = Square;
