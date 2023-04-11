#!/usr/bin/node
// a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:

const arg = parseInt(process.argv[2]);

if (Number.isInteger(parseInt(arg))) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
