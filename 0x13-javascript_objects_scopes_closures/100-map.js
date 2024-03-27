#!/usr/bin/node
const list = require('./100-data.js').list;

console.log(list);
const map1 = list.map((x, index) => x * index);
console.log(map1);
