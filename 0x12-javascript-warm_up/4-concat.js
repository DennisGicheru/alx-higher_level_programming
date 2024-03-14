#!/usr/bin/node

/* prints two arguments passed to it in the "is" format
 * example arg 1 : c
 * arg 2: cool
   result: c is cool */

const x = process.argv[2];
const y = process.argv[3];
console.log(x + ' is ' + y);
