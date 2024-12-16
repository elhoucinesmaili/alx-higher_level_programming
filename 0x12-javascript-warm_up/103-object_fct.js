#!/usr/bin/node
/* Update this script by adding a new function
incr that increments the integer value. */

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = function () {
  this.value += 1;  // Increment the value by 1
};

myObject.incr();  // First increment
console.log(myObject);

myObject.incr();  // Second increment
console.log(myObject);

myObject.incr();  // Third increment
console.log(myObject);
