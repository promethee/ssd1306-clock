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
FONT_SIZE = os.environ.get('FONT_SIZE', 38)
OFFSET_X = os.environ.get('OFFSET_X', 0)
OFFSET_Y = os.environ.get('OFFSET_Y', -8)
SHOW_DATE = "DATE"
SHOW_TIME = "TIME"
SHOW = os.environ.get('SHOW', SHOW_DATE)
WAIT = dict({
  "DATE": os.environ.get('WAIT_DATE', 1),
  "TIME": os.environ.get('WAIT_TIME', 5),
})


display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

def get_text():
  global SHOW
  return datetime.datetime.now().astimezone(None).strftime(
    "%H:%M" if SHOW == SHOW_TIME else "%a %d"
  )

font = ImageFont.truetype(RobotoMedium, FONT_SIZE)
(TEXT_WIDTH, TEXT_HEIGHT) = font.getsize(get_text())

im = Image.new("1", (WIDTH, HEIGHT), 0)
draw = ImageDraw.Draw(im)

def clear():
  display.fill(0)
  display.image(im)

def show_time():
  clear()
  text = get_text()
  draw.rectangle([0, 0, WIDTH, HEIGHT], fill=0)
  draw.text((OFFSET_X, OFFSET_Y), text, align='center', font=font, fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()

def show_emoji():
  clear()
  draw.rectangle([0, 0, WIDTH, HEIGHT], fill=0)
  font_smiley = ImageFont.truetype('./CODE2000.TTF', 28)
  draw.text((0, -4), "¯\_(ツ)_/¯", font=font_smiley, fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()

def show_credits(text):
  clear()
  draw.rectangle([0, 0, WIDTH, HEIGHT], fill=0)
  font = ImageFont.truetype(RobotoMedium, 24)
  draw.text((0, -4), text, font=font, fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()

show_emoji()
time.sleep(1)
show_credits("promethee")
time.sleep(1)
show_credits("@github")
time.sleep(1)

while True:
  SHOW = SHOW_TIME if SHOW == SHOW_DATE else SHOW_DATE
  show_time()
  time.sleep(WAIT[SHOW])
