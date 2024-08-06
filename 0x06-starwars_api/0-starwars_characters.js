#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

async function requestAsync(url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, _, body) {
      if (err) return reject(err);
      resolve(JSON.parse(body));
    });
  });
}
async function main() {
  const film = await requestAsync(baseUrl + process.argv[2]);
  for (const url of film.characters) {
    const character = await requestAsync(url);
    console.log(character.name);
  }
}
main();
