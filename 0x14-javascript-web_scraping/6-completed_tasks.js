#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);
  const BodyResults = JSON.parse(body);
  const task = {};
  for (let i = 0; i < BodyResults.length; i++) {
    const UserId = BodyResults[i].userId;
    if (BodyResults[i].completed) {
      task[UserId] = (UserId in task ? task[UserId] + 1 : 1);
    }
  }
  console.log(task);
});
