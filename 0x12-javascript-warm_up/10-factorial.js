#!/usr/bin/node
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : factorial(n - 1) * n;
}
console.log(factorial(parseInt(process.argv[2], 10)));
