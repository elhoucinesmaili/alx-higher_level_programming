#!/usr/bin/node
// A function that returns the reversed version of a list using `reduce`

exports.reverseList = function (list) {
  return list.reduce((acc, curr) => [curr, ...acc], []);
};
