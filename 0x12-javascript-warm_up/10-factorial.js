#!/usr/bin/node
// script that computes and prints a factorial
const n = process.argv[2];
function factorial (n) {
  if ((Number.isNaN(parseInt(n))) || (parseInt(n) <= 1)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const result = factorial(n);
console.log(result);
