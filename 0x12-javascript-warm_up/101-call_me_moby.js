#!/usr/bin/node
// 101-call_me_moby.js

exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};
