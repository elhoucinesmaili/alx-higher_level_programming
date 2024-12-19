#!/usr/bin/node
// A class Square that defines a square and inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the parent class constructor with width and height equal to size
  }
}

module.exports = Square;
