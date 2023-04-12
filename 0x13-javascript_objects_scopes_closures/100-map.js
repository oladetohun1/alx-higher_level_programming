#!/usr/bin/node
// script that imports an array and computes a new array.

const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map(function (element, index) {
  return (element * index);
});
console.log(mappedList);
