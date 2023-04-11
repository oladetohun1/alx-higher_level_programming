#!/usr/bin/node
// a script that prints a square

const arg = process.argv[2];
if (!Number.isInteger(parseInt(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
