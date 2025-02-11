const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch data (Status Code: ${response.statusCode})`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  const fetchCharacter = (index) => {
    if (index >= characterUrls.length) return;
    request(characterUrls[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      if (res.statusCode !== 200) {
        console.error(`Error: Unable to fetch character (Status Code: ${res.statusCode})`);
        return;
      }
      console.log(JSON.parse(charBody).name);
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});
