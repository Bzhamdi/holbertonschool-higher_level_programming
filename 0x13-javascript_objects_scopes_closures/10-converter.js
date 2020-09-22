#!/usr/bin/node
/* to string converter */
exports.converter = function (base) {
  return anyParam => anyParam.toString(base);
};
