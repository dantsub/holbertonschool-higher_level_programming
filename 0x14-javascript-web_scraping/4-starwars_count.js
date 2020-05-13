#!/usr/bin/node
const request = require('request');
request
  .get(process.argv[2], (err, response, body) => {
    if (!err) {
      let count = 0;
      const results = JSON.parse(body).results;
      results.forEach(attr => {
        if (attr.characters.find(character => character.endsWith('/18/'))) count++;
      });
      console.log(count);
    }
  });
