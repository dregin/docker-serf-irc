#!/bin/bash
# Linked Container's IP
serf_master_ip=`env|grep TCP_ADDR|cut -f2 -d'='`
/usr/bin/serf join ${serf_master_ip}:1337
