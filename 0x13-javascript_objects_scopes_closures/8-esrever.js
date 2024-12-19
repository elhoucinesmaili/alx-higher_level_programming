#!/usr/bin/node
// function that returns the reversed version of a list
exports.reverseList = function (list) {
  let newList = [];
  list.forEach((element, index) => {
    newList.unshift(element);
  });
  return newList;
};
