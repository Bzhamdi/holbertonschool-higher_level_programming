#!/usr/bin/node
var fs = require('fs');
var uglify = require("uglify-js");
var uglified = uglify.minify([process.argv[2], process.argv[3]]);
fs.writeFile(process.argv[4], uglified.code);
