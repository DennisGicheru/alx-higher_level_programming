#!/usr/bin/node
const Square2 = require('./5-square');

module.exports = class Square extends Square2 {
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
};
