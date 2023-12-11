#!/usr/bin/node
// Script to concatenate two arguments
'use strict';

// Check if both arguments are provided
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  // Handle cases when one or both arguments are missing
  console.log(process.argv[2] + ' is undefined');
}
