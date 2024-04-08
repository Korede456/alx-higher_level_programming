#!/usr/bin/node

let len = process.argv.length;

if (len < 3){
	console.log("No argument");
	return;
};
console.log(process.argv[2]);
