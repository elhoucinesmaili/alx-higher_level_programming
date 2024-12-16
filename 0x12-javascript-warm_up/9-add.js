#!/usr/bin/node
// Script that prints the addition of 2 integers.

const [a, b] = process.argv.slice(2).map(Number); // Destructure and convert to integers

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(a + b);
}
