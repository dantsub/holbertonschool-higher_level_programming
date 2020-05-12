#!/usr/bin/node
const request = require('request');
request
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
    console.log(err || JSON.parse(body).title);
  });
