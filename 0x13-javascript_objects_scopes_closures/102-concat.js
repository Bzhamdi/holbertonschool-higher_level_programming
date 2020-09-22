#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[4], fs.readFileSync(process.argv[2], 'utf-8') + fs.readFileSync(process.argv[3], 'utf-8'));
