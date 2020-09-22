#!/usr/bin/node
exports.esrever = function (list) {
  /* reverse list with js */
  const rev = [];

  for (let i = list.length - 1; i >= 0; --i) {
    rev.push(list[i]);
  }
  return rev;
};
