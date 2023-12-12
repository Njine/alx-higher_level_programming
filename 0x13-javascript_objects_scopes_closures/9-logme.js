#!/usr/bin/node
const count = 0;
exports.logMe = (function () {
  let count = 0;

  return function (item) {
    console.log(count + ': ' + item);
    count++;
  };
})();
