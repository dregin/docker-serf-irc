#!/bin/bash
# event caught - check it's type and stick message in FIFO, if it's the wee-serf
irc_in=/var/tmp/irc/irc.freenode.net/#serf-test/in
echo
echo "New event: ${SERF_EVENT}. Data follows..." > ${irc_in}
while read line; do
	echo "${line}\n" > ${irc_in}
done
