#!/usr/bin/node
const data = require('./101-data').dict;
const dict = {};
for (const key in data) {
  (dict[data[key]] === undefined) ? dict[data[key]] = [key] : dict[data[key]].push(key);
}
console.log(dict);
