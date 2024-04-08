#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length > 0) {
  const firstArg = parseInt(args[0]);
  if (!isNaN(firstArg)) {
    for (let i = 0; i < firstArg; i++) {
      let output = '';
      for (let j = 0; j < firstArg; j++) {
        output = output.concat('X');
      }
      console.log(output);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
