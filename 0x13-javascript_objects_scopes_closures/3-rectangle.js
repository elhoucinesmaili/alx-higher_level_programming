#!/usr/bin/node
// A class Rectangle that defines a rectangle

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // If conditions are not met, the object remains empty
  }

  // Method to print the rectangle using 'X'
  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
