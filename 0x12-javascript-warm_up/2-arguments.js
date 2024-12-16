#!/usr/bin/node
// Script that prints a message based on the number of arguments provided.

const argsCount = process.argv.slice(2).length;

switch (argsCount) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
