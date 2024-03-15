#!/usr/bin/node

// function that prints the addition of 2 integers
const x = process.argv[2];
const y = process.argv[3];
function add (a, b) {
  a = parseInt(x);
  b = parseInt(y);
  console.log(a + b);
} add();
