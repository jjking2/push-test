#!/bin/bash

# This cgi-bin script consumes data from a unix domain socket and
# sends them to a web client through server sent event (sse).
# Note that this script 'blocks' on the socket while data is not available;
# no peeking or polling done.

trap 'logger -s -t "sse-test.cgi" "trap: SIGINT"; exit 1' SIGINT
trap 'logger -s -t "sse-test.cgi" "trap: SIGQUIT"; exit 1' SIGQUIT
trap 'logger -s -t "sse-test.cgi" "trap: SIGTERM"; exit 1' SIGTERM
trap 'logger -s -t "sse-test.cgi" "trap: SIGPIPE"; exit 1' SIGPIPE
trap 'logger -s -t "sse-test.cgi" "trap: SIGKILL"; exit 1' SIGKILL

echo 'Cache-Control: no-cache'
echo 'Connection: keep-alive'
echo 'Content-type: text/event-stream'
echo ''

while true
do
	logger -s -t "sse-test.cgi" "reading..."
	#cat /tmp/push-test-fifo
	nc -Ul /tmp/sock
#	echo ''
#	echo ''
done

logger -s -t "sse-test.cgi" "done"

# Note: I first tried a fifo instead of a unix domain socket.
# It works fine on a terminal but not as an cgi; 'cat' does not block on the fifo.
