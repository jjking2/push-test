#!/bin/bash
echo 'Content-type: text/plain'
echo ''

# this cgi script writes a message to a unix domain socket which sse-test.cgi consumes and
# relays the message to a web client via server sent event (sse)

#echo 'data:' `date +%H:%M:%S` > /tmp/push-test-fifo
echo 'data:' `date +%H:%M:%S` | nc -UN /tmp/sock

echo 'OK'
