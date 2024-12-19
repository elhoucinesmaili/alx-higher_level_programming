#!/usr/bin/node
// A class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  // Method to calculate the area of the rectangle
  area() {
    return this.width * this.height;
  }

  // Method to calculate the perimeter of the rectangle
  perimeter() {
    return 2 * (this.width + this.height);
  }
}

module.exports = Rectangle;
