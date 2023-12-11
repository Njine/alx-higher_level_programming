#!/usr/bin/node
// Script to print a number if the first argument can be converted to an integer
'use strict';

// Try to convert the first argument to an integer
const number = parseInt(process.argv[2]);

// Check if the conversion is successful (not NaN)
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number:', number);
}
