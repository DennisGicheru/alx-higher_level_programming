#!/usr/bin/node

// convert first argument to integer and print number where possible
// else print "Not a number"
const x = parseInt(process.argv[2], 10);
if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My Number:' + ' ' + x);
}
