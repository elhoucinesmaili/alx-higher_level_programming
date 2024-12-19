#!/usr/bin/node
// A class Square that defines a square and inherits from Square

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint(c) {
    const char = c || 'X'; // Use 'X' if c is undefined
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
