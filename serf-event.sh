#!/bin/bash
# event caught - check it's type and stick message in FIFO, if it's the wee-serf
echo
echo "New event: ${SERF_EVENT}. Data follows..."
while read line; do
	printf "${line}\n"
done
