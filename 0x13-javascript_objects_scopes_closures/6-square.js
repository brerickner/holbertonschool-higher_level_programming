#!/usr/bin/node

const squareDad = require('./5-square');

class Square extends squareDad {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log(`${c}`.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
