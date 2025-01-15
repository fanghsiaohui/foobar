var http=require('http')
http.create.Server(function(request, response) {
    response.writeHead(200,
        {'Content-Type': 'text/plain'});
    respone.write('hello, world\n');
    response.end();
}).listen(9000);

console.log('something');
