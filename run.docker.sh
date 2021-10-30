#!/bin/sh
docker run -d --privileged --device /dev/spi.dev0.0:/dev/spi.dev0.0 --restart always --name clock promethee/ssd1306-clock:latest
