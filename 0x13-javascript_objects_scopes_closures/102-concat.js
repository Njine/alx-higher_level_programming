#!/usr/bin/node
const fs = require('fs');

try {
  const fArg = fs.readFileSync(process.argv[2], 'utf8');
  const sArg = fs.readFileSync(process.argv[3], 'utf8');
  fs.writeFileSync(process.argv[4], fArg + sArg);
  console.log('Concatenation successful!');
} catch (error) {
  console.error('Error:', error.message);
}
