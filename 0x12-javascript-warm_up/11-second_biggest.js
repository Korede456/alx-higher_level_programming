#!/usr/bin/node

if (process.argv.length <= 3){
	console.log(0);
}
else {
	let args = process.argv.slice(2);
	args.sort((a, b) => a - b);
	console.log(args[args.length - 2]);
}
