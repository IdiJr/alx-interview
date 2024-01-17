#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Make an API request to get film information
request(filmURL + filmNum, async function (err, res, body) {
  if (err) {
    console.error('Error fetching film information:', err);
    return;
  }

  // Parse the response body to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Iterate through the character URLs and fetch character information
  // Make a request to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) {
          console.error('Error fetching character information:', err);
          reject(err);
          return;
        }

        // Parse the character information and print the character's name
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
