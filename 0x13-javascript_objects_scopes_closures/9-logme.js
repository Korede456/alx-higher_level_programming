#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  if (item !== undefined) {
    console.log(`${count}: ${item}`);
    count += 1;
  }
};
