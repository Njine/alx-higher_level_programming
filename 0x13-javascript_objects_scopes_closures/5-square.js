#!/usr/bin/node
// JS script to define a class, extends to another class
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
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
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
