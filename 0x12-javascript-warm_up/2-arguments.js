#!/usr/bin/node
const len = process.argv.length;
console.log(len < 3 ? 'No argument' : len === 3 ? 'Argument Found' : 'Arguments found');
