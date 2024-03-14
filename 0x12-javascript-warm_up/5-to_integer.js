#!/usr/bin/node

// convert first argument to integer and print number where possible
// else print "Not a number"
console.log(parseInt(process.argv[2], 10) ? 'My number: ' + parseInt(process.argv[2], 10) : 'Not a number');
