#!/usr/bin/node
// A class Rectangle that defines a rectangle

class Rectangle {
  constructor (width, height) {
    this.width = width || 1;  // Default to 1 if no valid width is provided
    this.height = height || 1;  // Default to 1 if no valid height is provided
  }
}

module.exports = Rectangle;
