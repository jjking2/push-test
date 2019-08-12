#!/bin/bash

# this cgi-bin script sends data through event stream to a web client

echo 'Cache-Control: no-cache'
echo 'Connection: keep-alive'
echo 'Content-type: text/event-stream'
echo ''

while true
do
	echo 'data:' `date +%H:%M:%S`
	echo ''
	echo ''
	sleep 10
done
