#!/usr/bin/node
exports.esrever = function (list) {
  /* reverse list with js */
  const rev = [];
  let i = list.length;
  for (i - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
