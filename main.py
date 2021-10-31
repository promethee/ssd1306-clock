#!/usr/bin/python
import os
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import datetime
import time
from fonts.ttf import RobotoMedium

WIDTH = os.environ.get('WIDTH', 128)
HEIGHT = os.environ.get('HEIGHT', 32)
ROTATE = os.environ.get('ROTATE', False)
FONT_SIZE = os.environ.get('FONT_SIZE', 40)
OFFSET_X = os.environ.get('OFFSET_X', 0)
OFFSET_Y = os.environ.get('OFFSET_Y', -8)
SHOW_DATE = "DATE"
SHOW_TIME = "TIME"
SHOW = os.environ.get('SHOW', SHOW_DATE)

display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

def get_text():
  global SHOW
  return datetime.datetime.now().astimezone(None).strftime(
    "%H:%M" if SHOW == SHOW_TIME else "%a %d"
  )

font = ImageFont.truetype(RobotoMedium, FONT_SIZE)
(TEXT_WIDTH, TEXT_HEIGHT) = font.getsize(get_text(INFO_TIME))

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

def show_credits():
  clear()
  draw.rectangle([0, 0, WIDTH, HEIGHT], fill=0)
  font = ImageFont.truetype(RobotoMedium, 16)
  draw.text((0, -4), "github.com \n /promethee ", font=font, fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()

show_credits()
time.sleep(3)

while True:
  show_time()
  time.sleep(5)
  SHOW = SHOW_TIME if SHOW == SHOW_DATE else SHOW_DATE
