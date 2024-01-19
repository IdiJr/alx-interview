#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2] + '/';
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + movieId, (error, response, body) => {
  if (error) {
    console.error('Error fetching film information:', error);
  } else if (response.statusCode !== 200) {
    console.error('HTTP Error fetching film information. Status Code:', response.statusCode);
  } else {

    // Parse the response body to get the list of character URLs
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    if (characters && characters.length > 0) {
      // Iterate through the character URLs and fetch character information
      // Make a request to each character URL
      characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error fetching character information:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('HTTP Error fetching character information. Status Code:', charResponse.statusCode);
          } else {
            // Parse the character information and print the character's name
            console.log(JSON.parse(charBody).name);
          }
        });
      });
    } else {
      console.error('No characters found for the specified movie ID.');
    }
  }
});
