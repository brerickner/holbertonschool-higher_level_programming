#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

const fileStream = fs.createWriteStream(file);
request(url).pipe(fileStream);
