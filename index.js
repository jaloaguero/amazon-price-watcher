//I am using express, node, body-parser
//
//this is such a fucking mess lol

//essentially declears stuff
const { readFile, readFileSync } = require('fs').promises;
//init express
const express = require('express')
//init body-parser
const bodyParser = require('body-parser');
//declares app as express
const app = express();

//this lets me use body-parser with express tbh idk what it does 
app.use(bodyParser.urlencoded({ extended: true }));

//TODO: make sure that these files actually are read
//Allows reference to other files in this folder. Add more if needed
app.use(express.static('./'));
app.use(express.static('./python_files'))
app.use(express.static('./html_files'))

//DONE DECLARING STUFF
////////////////////////////////////////////////////////////////////////////////////



//Call periodic_checker will always run and check hourly all the websites user input
//starts when index.js starts not tied to the GET POST stuff
const periodic_checker_module = require('./periodic_checker')
periodic_checker_module.periodicCheck()

//sends out the popup.html file
app.get('/', async(request, response) => {
	response.send(await readFile('./html_files/popup.html', 'utf8'));

})

//here we give a response in localhost:3000/confirmation
app.post("/confirmation", async(request, response) => {
	//here is where we do everything before we send the response
	const new_site_module = require('./new_site');
	
	//using body-whatever to grab URL from the popup.html form and saves it to var getURL
	//then is passed to new_site_module declared above, references webURL and passes getURL to it
	var getURL = request.body.URL;
	var getDesiredPrice = request.body.userPrice;
	new_site_module.init_new_site(getURL, getDesiredPrice);

	//TODO: Make an actual html file and pass arguments to it as opposed to this ugly thing. 
	//sends out what we have saved here plus a message
	response.send(await readFile('./html_files/confirmation.html', 'utf8'));
})
//???? im not sure its just the thing i copied off the internet to make the server? 
var port_num = 3000;

app.listen(process.env.PORT || port_num, () => console.log(`App avaialbe on http://localhost:`+port_num))
