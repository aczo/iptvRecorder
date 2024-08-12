#!/bin/bash
. env.sh
cd $PYTHON_DIR
ffplay -vf scale=1280:-1 udp://$($PYTHON getcurstream.py)":$UDP_PORT"
