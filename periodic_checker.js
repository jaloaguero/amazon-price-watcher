//Runs periodic_checker.py every hour or so

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

//1,000ms = 1 second
//1,000 x 60 = 60,000ms = 1 minute
//60,000 x 60 = 3,600,000 = 1 hour

async function periodicCheck() {
	
	var timesLooped = 0;

	while(1 == 1) {
		await sleep(3600000);

		console.log(timesLooped);
		timesLooped = timesLooped + 1;

 
  	const {spawn} = require('child_process'); 
  	const childPython = spawn('python3', ['periodic_checker.py']);

  	childPython.stdout.on('data', (data) => {
			console.log(`stdout: ${data}`);
 		});              
		childPython.stderr.on('data', (data) => {
			console.error(`stderr: ${data}`);
		});
	}
 









	}

module.exports.periodicCheck = periodicCheck;
