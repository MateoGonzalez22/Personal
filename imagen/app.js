const express = require('express')
const mysql = require('mysql2');

const app = express()
const port = 3001

app.get('/', (req, res) => {
  res.send('Web TUTE!')
})

app.listen(port, () => {
  console.log(`Listening on port: ${port}`)
})

setTimeout(() => {
  const connection = mysql.createConnection({
    host: 'mysql',
    user: 'root',
    password: 'politute'
  });
  connection.connect(function (err) {
    if (err) {
      console.log(err);
    } else {
      console.log('MySQL Conectado correctamente!');
    }
  });
}, 5000);