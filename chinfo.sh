#!/bin/bash
. env.sh
# shellcheck disable=SC2164
# shellcheck disable=SC2164
cd $PYTHON_DIR
ffprobe -print_format json -show_programs udp://$($PYTHON getcurstream.py)":$UDP_PORT"
