#!/usr/bin/python
import os
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import datetime
import time

INFO_TIME = "INFO_TIME"
INFO_DATE = "INFO_DATE"
info_type = INFO_DATE

i2c = busio.I2C(SCL, SDA)

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32

display = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

ROTATE = os.environ.get('ROTATE', False)

def get_text(info_type):
  return datetime.datetime.now().strftime(
    "%H:%M" if info_type == INFO_TIME else "%a %d"
  )

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", DISPLAY_HEIGHT)
(TEXT_WIDTH, TEXT_HEIGHT) = font.getsize(get_text(INFO_TIME))

im = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT), 0)
draw = ImageDraw.Draw(im)

while True:
  text = get_text(info_type)
  display.fill(0)
  draw = ImageDraw.Draw(im)
  draw.rectangle([0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT], fill=0)
  draw.text((0, 0), text, font=font, fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()
  info_type = INFO_TIME if info_type == INFO_DATE else INFO_DATE
  time.sleep(5)
