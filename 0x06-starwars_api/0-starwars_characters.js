#!/usr/bin/node

const { exit } = require('process');
const request = require('request');
const url = 'https://swapi.dev/api/films/';
const argument = process.argv[2];

if (argument === undefined) {
  exit();
}

request(url + argument, (error, response, body) => {
  if (!error) {
    const chars = JSON.parse(body).characters;
    orderPrinter(chars, 0);
  } else {
    console.log(error);
  }
});

function orderPrinter (chars, n) {
  if (n >= chars.length) {
    return;
  }
  request(chars[n], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      orderPrinter(chars, n + 1);
    } else {
      console.log(error);
    }
  });
}
