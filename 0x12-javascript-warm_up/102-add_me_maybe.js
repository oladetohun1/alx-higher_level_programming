#!/usr/bin/node
// a function that increments and calls a function.

const addMeMaybe = function (number, theFunction) {
  number++;
  return theFunction(number);
};
module.exports = { addMeMaybe };
