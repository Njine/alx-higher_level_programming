#!/usr/bin/node
// 102-add_me_maybe.js
exports.addMeMaybe = function (number, theFunction) {
  theFunction.call(this, ++number);
};
