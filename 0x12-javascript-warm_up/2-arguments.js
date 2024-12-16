#!/usr/bin/node
// A script that prints a message depending on the number of arguments passed

const args = process.argv.slice(2);

switch (args.length) {
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
