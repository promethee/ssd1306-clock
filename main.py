#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import datetime
import time
from fonts.ttf import RobotoMedium

i2c = busio.I2C(SCL, SDA)

WIDTH = os.environ.get('WIDTH', 128)
HEIGHT = os.environ.get('HEIGHT', 32)
ROTATE = os.environ.get('ROTATE', False)
FONT_SIZE = int(os.environ.get('FONT_SIZE', 38))
OFFSET_X = os.environ.get('OFFSET_X', 0)
OFFSET_Y = os.environ.get('OFFSET_Y', -4)
SHOW_DATE = "DATE"
SHOW_TIME = "TIME"
SHOW = os.environ.get('SHOW', SHOW_DATE)
WAIT = dict({
  "DATE": os.environ.get('WAIT_DATE', 1),
  "TIME": os.environ.get('WAIT_TIME', 5),
})

fonts = dict({
  "emoji": ImageFont.truetype('./CODE2000.TTF', 24),
  "credits": ImageFont.truetype(RobotoMedium, 24),
  "DATE": ImageFont.truetype(RobotoMedium, FONT_SIZE),
  "TIME": ImageFont.truetype(RobotoMedium, FONT_SIZE),
})

def get_text():
  global SHOW
  display_format = "%H:%M" if SHOW == SHOW_TIME else "%a %d"
  return datetime.datetime.now().astimezone(None).strftime(display_format)

def clear():
  display.fill(0)
  display.image(im)

display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

emoji = "¯\_(ツ)_/¯"
platform = "@github"
author = "promethee"

im = Image.new("1", (WIDTH, HEIGHT), 0)
draw = ImageDraw.Draw(im)

def show(text, font):
  clear()
  size = font.getsize(text)
  draw.rectangle([0, 0, WIDTH, HEIGHT], fill=0)
  draw.text((OFFSET_X + ((WIDTH/2)-(size[0]/2)), OFFSET_Y), text, align='center', font=font, fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()

for text,font_key in [(emoji, "emoji"), (author, "credits"), (platform, "credits")]:
  show(text, fonts[font_key])
  time.sleep(1)

while True:
  SHOW = SHOW_TIME if SHOW == SHOW_DATE else SHOW_DATE
  show(get_text(), fonts[SHOW])
  time.sleep(WAIT[SHOW])
