#!/usr/bin/node
const SqInherit = require('./5-square');

class Square extends SqInherit {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; ++i) {
      let str = '';
      for (let j = 0; j < this.width; ++j) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
