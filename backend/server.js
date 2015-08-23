var http = require('http');
var config = require('./config');
var port = config.port;

var server = http.createServer(function(req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>Hello World !</h1>');
}).listen(port, function() {
    console.log('Server Running on port ' + port);
});
