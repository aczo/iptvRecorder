#!/bin/bash
. env.sh
cd $PYTHON_DIR
today=$(date +"%Y-%m-%d %H_%M_%S")
addr=$($PYTHON getcurstream.py)
file_name=$RECORDINGS"/"$today" "$($PYTHON channelname.py $addr)".mp4"
echo "Recording to: "$file_name
ffmpeg -re -i "udp://"$addr":$UDP_PORT?overrun_nonfatal=1&fifo_size=50000000" -ignore_unknown -map 0:0 -c:v copy -map 0:1 -c:a aac "$file_name"
