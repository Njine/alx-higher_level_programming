#!/usr/bin/node
// JS FUNCTION TO REVERSE A LIST
exports.esrever = function (list) {
  return list.reduce((newList, element) => [element, ...newList], []);
};
