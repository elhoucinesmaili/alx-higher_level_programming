#!/usr/bin/node
// Script that prints two arguments passed to it in the format: " is "

const args = process.argv.slice(2);
console.log(`${args[0] || 'undefined'} is ${args[1] || 'undefined'}`);
