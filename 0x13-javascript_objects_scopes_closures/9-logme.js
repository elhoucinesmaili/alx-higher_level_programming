#!/usr/bin/node
// A function that prints no. of args already printed and new argument value

exports.logMe = (function () {
  let i = 0;
  return function (item) {
    console.log(i + ': ' + item);
    i++;
  };
})();
