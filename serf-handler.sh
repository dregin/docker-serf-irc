#!/bin/bash
# event caught - check it's type and stick message in FIFO, if it's the wee-serf
irc_in="/var/tmp/irc/irc.freenode.net/\#serf-test/in"
if [ -f `${irc_in}` ];
then
	echo "New event: ${SERF_EVENT}. Data follows..." > /var/tmp/irc/irc.freenode.net/\#serf-test/in
	while read line; do
		echo ${line} > /var/tmp/irc/irc.freenode.net/\#serf-test/in
	done
fi
