#!/bin/sh
# --privileged : required to access hardware
# -v /etc/localtime:/etc/localtime : allow to have the same timezone setting inside the container
# --device /dev/i2c-1:/dev/i2c-1 & --device /dev/spidev0.0:/dev/spidev0.0 : required to access the PiOLED
# --restart always : required to prevent the clock from stopping
docker run -d -e ROTATE=False --privileged -v /etc/localtime:/etc/localtime --device /dev/i2c-1:/dev/i2c-1 --device /dev/spidev0.0:/dev/spidev0.0 --restart always --name $(basename "$PWD") $USER/$(basename "$PWD"):latest
