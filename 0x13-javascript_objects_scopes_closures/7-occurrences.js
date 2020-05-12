#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((total, actual) => actual === searchElement ? total + 1 : total, 0);
};
