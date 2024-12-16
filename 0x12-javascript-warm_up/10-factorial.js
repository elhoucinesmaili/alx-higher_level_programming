#!/usr/bin/node
// Script that computes and prints a factorial.

const num = parseInt(process.argv[2]);

function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

console.log(factorial(num));
