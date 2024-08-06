#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
request(baseUrl + process.argv[2], function (error, _, body) {
  if (error) return console.error(error);
  const re = /"characters":\[(.*)\],"planets":/;
  const characters = re.exec(body)[1].replaceAll('"', '').split(',');
  for (const url of characters) {
    request(url, function (err, _, body) {
      if (!err) console.log(JSON.parse(body).name);
    });
  }
});
