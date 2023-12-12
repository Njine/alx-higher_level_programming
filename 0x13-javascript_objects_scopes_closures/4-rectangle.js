#!/usr/bin/node
// JS script to define a class, creates instance methods to print, rotate, and double the rectangle
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // Creating an empty object if width or height is not valid
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let count = 0; count < this.height; count++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const holder = this.width;
    this.width = this.height;
    this.height = holder;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
