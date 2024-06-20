#!/usr/bin/node
// 2-rectangle.js

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = null;
      this.height = null;
    }
  }
};
