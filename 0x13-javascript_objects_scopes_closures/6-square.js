#!/usr/bin/node
// 6-square.js

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        shape += c;
      }
      console.log(shape);
    }
  }
}

module.exports = Square;
