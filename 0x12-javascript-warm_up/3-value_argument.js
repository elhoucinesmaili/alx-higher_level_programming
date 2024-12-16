#!/usr/bin/node
// Script that prints the first argument passed to it or a default message if none is provided.

const [,, firstArg] = process.argv;

console.log(firstArg || 'No argument');
