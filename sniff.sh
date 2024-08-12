#!/bin/bash
. env.sh
sudo tcpdump -B 5000 -n -p -i $INTERFACE ip multicast
