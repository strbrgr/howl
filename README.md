# Howl

<!--toc:start-->
- [Howl](#howl)
  - [What is this all about?](#what-is-this-all-about)
  - [Documentation](#documentation)
    - [Installing Docker on your Pi](#installing-docker-on-your-pi)
  - [Things learned along the way](#things-learned-along-the-way)
<!--toc:end-->

## What is this all about?

I regularly scream during sleep at night. Sometimes once sometimes plenty of times. Most of the times my wife has to wake me up. The number of screams correlates with the stress level within my day-to-day life, so I thought it would be a fun to come up with a project that uses Deep Learning to analyze my screaming behavior.

## Documentation

### Installing Docker on your Pi

```sh
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

### Using arecord to record via my external Microphone
When I started this project I thought that I would need python and the PyAudio library to record sound through my external microphone. While this might work it was total overkill once I discovered [arecord](https://linux.die.net/man/1/arecord). Arecord is a command-line sound recorder and player for ALSA soundcard driver and can be used super easy with a cronjob and a shell script:

```shell
#!/bin/bash

timeout 28800 /usr/bin/arecord -D plughw:2,0 -f cd -t wav --max-file-time 3600 --use-strftime "/home/jo/Desktop/howl/audio/%Y/%m/%d/listen-%H-%M-%v.wav"

```

This will record the sound for 8 hours and write to a seperate file/folder every hour once I created the following cronjob:
```shell
0 22 * * * /home/jo/Desktop/howl/audio/record_audio.sh
```

I normally pass out around 10pm and get up around 5am, so recording for 8 hours makes sense.

## Things learned along the way
