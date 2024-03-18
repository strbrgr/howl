#!/bin/bash

file_name="howl_$(date +'%Y-%m-%d').wav"

arecord -D plughw:2,0 --duration=28800 "$file_name"
