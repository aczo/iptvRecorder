#!/bin/bash
. env.sh
cd $PYTHON_DIR
ffprobe -print_format json -show_programs udp://$($PYTHON getcurstream.py)":$UDP_PORT"
