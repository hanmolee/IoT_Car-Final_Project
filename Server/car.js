var express = require('express');
var bodyParser = require('body-parser');
var sql = require('mysql');
var app = express();

var blinkers = require('./Blinkers');
var distance = require('./Distance');
//var handle = require('./Handle');

var Server = app.listen(3001, function()
{
    console.log('3001 Port -> Running');
});

app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

app.get('/blinkers',blinkers.selectBlinkers);
app.post('/blinkers',blinkers.insertBlinkers);

//app.post('/handle',handle.insertHandle);

app.get('/distance',distance.selectDistance);
app.post('/distance',distance.insertDistance);
