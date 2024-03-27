#!/usr/bin/node
let list = require('./100-data.js').list;

console.log(list);
let map1 = list.map((x, index) => x * index);
console.log(map1);
