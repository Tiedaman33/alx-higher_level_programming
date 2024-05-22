#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Usage: ./writeToFile.js <file path> <string to write>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to the file:', err);
  } else {
    console.log('File written successfully.');
  }
});
