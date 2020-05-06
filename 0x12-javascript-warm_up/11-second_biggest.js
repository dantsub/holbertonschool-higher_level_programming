#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const listNumber = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b)
    .reverse();
  console.log(listNumber[1]);
}
