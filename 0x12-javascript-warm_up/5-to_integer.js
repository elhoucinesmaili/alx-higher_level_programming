#!/usr/bin/node
// Script that prints "My number: <first argument converted to integer>"
// if the first argument can be converted to an integer.

const arg = process.argv[2];
const number = parseInt(arg);

console.log(Number.isNaN(number) ? 'Not a number' : `My number: ${number}`);
