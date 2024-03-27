#!/usr/bin/node

const Rectangle = require('./4-rectangle');
export default class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
