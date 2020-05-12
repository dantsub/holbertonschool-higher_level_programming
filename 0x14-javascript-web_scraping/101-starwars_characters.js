#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (let index = 0; index < characters.length; index++) {
      request(characters[index], (err, response, body) => {
        console.log(characters[index]);
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
