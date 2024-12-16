#!/usr/bin/node
// Script that prints a square of "X" characters.

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(size); // Create one row of "X"s
  for (let i = 0; i < size; i++) {
    console.log(row); // Print the row size times
  }
}
