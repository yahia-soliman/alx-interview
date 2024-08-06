#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/';
request(baseUrl + 'films/' + process.argv[2], function (error, response, body) {
  if (error) return console.error(error);
  const data = JSON.parse(body);
  for (const url of data.characters) {
    request(url, function (err, res, body) {
      if (err) return console.error(err);
      console.log(JSON.parse(body).name);
    });
  }
});
