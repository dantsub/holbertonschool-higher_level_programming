#!/usr/bin/node
if (typeof (process.argv[2]) === 'undefined') {
  console.log('Missing number of occurrences');
}
if (process.argv[2] > 0) {
  let count = process.argv[2];
  while (count) {
    console.log('C is fun');
    count--;
  }
}
