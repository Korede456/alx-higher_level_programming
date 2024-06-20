#!/usr/bin/node
// 3-rectangle.js

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
      this.print = function (width, height) {
        for (let i = 0; i < height; i++) {
          let shape = '';
          for (let j = 0; j < width; j++) {
            shape += 'X';
          }
          console.log(shape);
        }
      };
    }
  }
};
