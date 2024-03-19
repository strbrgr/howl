#!/bin/bash

timeout 28800 /usr/bin/arecord -D plughw:2,0 -f cd -t wav --max-file-time 3600 --use-strftime "/home/jo/Desktop/howl/audio/export/%Y/%m/%d/listen-%H-%M-%v.wav"
