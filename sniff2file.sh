#!/bin/bash
. env.sh
sudo tcpdump -i $INTERFACE -s 65535 -w $1
