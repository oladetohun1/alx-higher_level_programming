#!/usr/bin/node
const { dict } = require('./101-data');

const result = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = [...(acc[value] || []), key];
  return acc;
}, {});

console.log(result);
