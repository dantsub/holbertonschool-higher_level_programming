#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const tasks = {};
    todos.forEach((todo) => {
      if (todo.completed && tasks[todo.userId] === undefined) {
        tasks[todo.userId] = 0;
      }
      if (todo.completed) {
        tasks[todo.userId] += 1;
      }
    });
    console.log(tasks);
  }
});
