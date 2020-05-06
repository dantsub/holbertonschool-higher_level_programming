#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
if (isNaN(number)) {
  console.log('Missing size');
}
for (let i = 0; i < number; i++) {
  console.log('X'.repeat(number));
}
