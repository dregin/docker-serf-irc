#!/bin/bash
irc_nick=a`hostname`     
irc_home=/var/tmp/irc                                           
/usr/bin/ii -i ${irc_home} -s irc.freenode.net -n ${irc_nick} -f ${irc_nick}
