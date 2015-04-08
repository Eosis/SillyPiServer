#!/usr/local/bin/node
var http = require('http');
var counter = 0;
var server = http.createServer(function(req, res) {
  res.writeHead(200);
  if (counter++ % 2 === 0) {
  	stringToWrite = 'ON\r\n\r\n';
  } else {
  	stringToWrite = 'OFF\r\n\r\n'
  }
  res.end(stringToWrite);
});
server.listen(8080);