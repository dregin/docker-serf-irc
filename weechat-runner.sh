#!/bin/bash
irc_nick=`hostname`                                                
/usr/bin/weechat-curses irc://${irc_nick}@irc.freenode.net/serf-test
