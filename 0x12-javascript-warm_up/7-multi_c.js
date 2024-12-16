#!/usr/bin/node
// Script that prints "C is fun" x times.

const count = parseInt(process.argv[2]);

if (!Number.isInteger(count)) {
  console.log('Missing number of occurrences');
} else {
  Array.from({ length: count }).forEach(() => console.log('C is fun'));
}
