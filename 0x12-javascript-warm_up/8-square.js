#!/usr/bin/node

const n = process.argv[2];

if (Number.isNaN(parseInt(n)) || (n === undefined)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
}
