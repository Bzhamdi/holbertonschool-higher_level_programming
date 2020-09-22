#!/usr/bin/node
let soMany = 0;
exports.logMe = function (item) {
  console.log(soMany + ': ' + item);
  soMany++;
};
