#!/usr/bin/node
// function that returns the reversed version of a list
exports.reverseList = function (list) {
  return list.reduce((acc, curr) => [curr, ...acc], []);
};
