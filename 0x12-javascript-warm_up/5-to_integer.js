#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
console.log(isNaN(number) ? 'Not a number' : `My number: ${number}`);
