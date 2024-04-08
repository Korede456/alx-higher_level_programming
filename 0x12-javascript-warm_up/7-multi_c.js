#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length != 0) {
	firstArg = args[0];
	if (firstArg < 0){
		return;
	} else {
		for (let i = 0; i < firstArg; i++){
			console.log("C is fun");
		};
	};
}else {
	console.log("Missing number of occurrences");
};
