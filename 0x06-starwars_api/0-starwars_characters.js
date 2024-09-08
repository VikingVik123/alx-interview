#!/usr/bin/node
const url = "https://swapi-api.hbtn.io/api"
const request = require('request');

if (process.argv.length > 2) {
    const movieId = process.argv[2];
    request(`${url}/films/${movieId}/`, (err, _, body) => {
        if (err) {
          console.log(err);
        }
        const characters = JSON.parse(body).characters;
        const charactersName = characters.map(
            url => new Promise((resolve, reject) => {
            request(url, (promiseErr, __, charactersReqBody) => {
                if (promiseErr) {
                    reject(promiseErr);
                }
                resolve(JSON.parse(charactersReqBody).name);
            });
        }));

    Promise.all(charactersName)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.log(allErr));
    });
}