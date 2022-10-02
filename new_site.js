//calls periodic_checker.py

function init_new_site(URL, desiredPrice) {
	
	const {spawn} = require('child_process');

	const childPython = spawn('python3', ['new_site.py', URL, desiredPrice]);
	
	childPython.stdout.on('data', (data) => { 
		console.log(`stdout: ${data}`);
	});
	//just handles an error in case stuff didn't work on the python end.
	childPython.stderr.on('data', (data) => {
		console.error(`stderr: ${data}`);
	});
}



//makes our function webURL exportable
module.exports.init_new_site = init_new_site;
