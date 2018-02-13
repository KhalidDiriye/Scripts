#!/bin/bash
# Khalid Diriye
# Search through network logs using awk and find IP and timestamps

grep -F $1 | awk '{match($0,/inside:[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/); ip = substr($0,RSTART,RLENGTH) ; match($1,/[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]/); timestamp = substr($1,RSTART,RLENGTH) ; print timestamp "," substr(ip,8)}' 