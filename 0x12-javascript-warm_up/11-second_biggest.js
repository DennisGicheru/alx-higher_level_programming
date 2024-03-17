#!/usr/bin/node

let biggest = 0;
let i = 0;
const arr = [];

for (i = 2; i < process.argv.length; i++) {
  if (!Number.isNaN(process.argv[i])) {
    arr[i - 2] = Number.parseInt(process.argv[i]);
  }
}
if (arr.length > 2) {
  biggest = Math.max.apply(null, arr);
  i = arr.indexOf(biggest);
  arr[i] = -Infinity;
  biggest = Math.max.apply(null, arr);
}
console.log(biggest);
