#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  /* return nb occ */
  let occ = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occ++;
    }
  }
  return (occ);
};
