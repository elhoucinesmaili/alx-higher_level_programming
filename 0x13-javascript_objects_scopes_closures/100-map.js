#!/usr/bin/node
// A function that converts number from base 10 to another passed as argument

exports.converter = function (base) {
  return (num) => num.toString(base);
};
