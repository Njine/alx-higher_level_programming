#!/usr/bin/node
// JS script to define class that inherits from another class
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint(c = 'X') {
    for (let count = 0; count < this.height; count++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;