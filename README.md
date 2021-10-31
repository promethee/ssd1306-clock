# ssd1306-clock

A docker image to use with a raspberry zero and the [PiOLED ssd1306 hat](https://www.adafruit.com/product/3527). 
  
Show the time...  

¯\\_(ツ)_/¯. 
  
run this container with:  

```
docker run -d -e ROTATE=False --privileged -v /etc/localtime:/etc/localtime --device /dev/i2c-1:/dev/i2c-1 --device /dev/spidev0.0:/dev/spidev0.0 --restart always --name clock promethee/ssd1306-clock:latest
```

Be sure to use the correct `i2c` and `spi` device


![https://www.adafruit.com/product/3527](https://raw.githubusercontent.com/promethee/ssd1306-clock/main/3527-04.jpg)
