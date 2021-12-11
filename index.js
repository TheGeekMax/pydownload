const express = require("express");
const cors = require('cors');
const fs = require('fs');

const PORT = 8080;
const app = express()

app.use(express.json(),cors())

app.get("/ytdl/getdata",async (req,res) =>{
	let rawdata = fs.readFileSync('data.json');
	let data = JSON.parse(rawdata);
	res.status(200).send(data)
})

app.listen(
	PORT,
	() => {
		console.log(`lancée sur http://localhost:${PORT}`)
});