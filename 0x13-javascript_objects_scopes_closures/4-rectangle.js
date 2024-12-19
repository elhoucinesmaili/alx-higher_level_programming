#!/usr/bin/node
// class Rectangle that defines a rectangle with additional methods
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('*'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width]; // Using destructuring for a cleaner swap
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  area () {
    return this.width * this.height;
  }
}
module.exports = Rectangle;
