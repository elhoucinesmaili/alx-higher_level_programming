#!/usr/bin/node

const { list } = require('./100-data');

console.log(list);
const newList = list.map(function (element, idx) {
  return element * idx;
});
console.log(newList);
