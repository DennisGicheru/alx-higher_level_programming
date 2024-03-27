#!/usr/bin/node

exports.esrever = function (list) {
  const reverseArr = [];
  for (let i = 0, len = list.length - 1; i < list.length; i++, len--) {
    reverseArr[i] = list[len];
  }

  return reverseArr;
};
