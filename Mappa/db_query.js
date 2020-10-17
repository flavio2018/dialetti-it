const mysql = require('mysql')
const express = require('express')
const cors = require('cors')
const app = express()
const port = 8080

app.use(cors())

var corsOptions = {
	origin: 'localhost:80',
	optionsSuccessStatus: 200
}

app.get('/db', cors(corsOptions), (req, res) => {
	var con = mysql.createConnection({
	  host: "localhost",
	  user: "root",
	  password: "password",
	  database: "dialetti_it"
	});

	con.connect(function(err) {
	  if (err) throw err;
	  con.query("SELECT * FROM Regioni", function (err, result, fields) {
	    if (err) throw err;
	    res.jsonp(result);
	    });
	  });
	});

app.get('/simple_query', cors(corsOptions), (req, res) => {
	columns = req.query.columns;
	tables = req.query.tables;
	conditions = req.query.conditions;

	var con = mysql.createConnection({
		host: "localhost",
		user: "root",
		password: "password",
		database: "dialetti_it"
	});

	con.connect(function(err) {
		if (err) throw err;
		query = "SELECT " + columns +
		 " FROM " + tables + " WHERE " + conditions + ";";

		con.query(query,
			function (err, result, fields) {
				if (err) throw err;
				res.jsonp(result);
			});
	});
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
}) 

