#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.

const arg = process.argv.slice(2).map(Number);

function secondMaxNumber (arr) {
  arr = arr.sort((a, b) => b - a);
  return arr[1] || 0;
}

console.log(secondMaxNumber(arg));
