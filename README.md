# push-test

This is a demonstration of javascript server sent event at client side and bash cgi scripts providing data using a unix domain socket.
One thing to note here is code on the server side blocks when data is unavailable.
It does not poll data, reducing unnecessary overhead.

## sse-test.html

This html page contains a simple javascript code to use EventSource to get a status update from the server.

## sse-test.cgi

This CGI script uses 'nc' (netcat) to consume data from a unix domain socket and pushes it to the client.
Netcat opens and closes the connection each time it receives the data produced from the data provider, fifo-test.cgi.

Problem: I am working on an unsolved problem; the script keeps running even if after the client disconnected.

## fifo-test.cgi

Wrong name: fifo is once used but abandoned due to some problem (described in sse-test.cgi code)

This CGI script is meant to called to provide data to sse-test.cgi thorugh the unix socket.

## Test environment

Server side: Raspbery Pi 3+ with Raspbian (Buster) with + Apache/2.4.38 installed

Client: Firefox 68.1 under Windows 10
