#!/usr/bin/node

const fs = require('fs').promises;
const { argv } = require('process');

async function mergeFiles() {
  try {
    const data1 = await fs.readFile(argv[2], 'utf8');
    await fs.writeFile(argv[4], data1, 'utf8');
    
    const data2 = await fs.readFile(argv[3], 'utf8');
    await fs.writeFile(argv[4], data2, { flag: 'a' }, 'utf8');
  } catch (err) {
    console.error(err);
  }
}

mergeFiles();
