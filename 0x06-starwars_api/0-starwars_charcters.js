#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: ./0-starwars_characters.js <Movie ID>');
    process.exit(1);
  }


const movieId = process.argv[2] + '/';
const apiURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film information
request(apiURL, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('HTTP Error:', response.statusCode);
    } else {
      // Parse the response body to get the list of character URLs
        const filmData = JSON.parse(body);
      const characters = filmData.characters;

  // Iterare through the character URLs and fect character information
  // Make a request to each character URL
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
      } else if (charResponse.statusCode !== 200) {
        console.error('HTTP Error:', charResponse.statusCode);
      } else {
        // Parse the charcter nformation and print the character's name Resolve the promise to indicate completion
        const charData = JSON.parse(charBody);
        console.log(charData.name);
    }
  });
});
}
});
