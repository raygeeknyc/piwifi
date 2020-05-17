#!/usr/bin/python3
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()


HOST="localhost"
SSID="----"
IP="none yet"
resolved=False
while not resolved:
  # Draw a black filled box to clear the image.
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  try:
    cmd = "iwgetid -r"
    SSID = subprocess.check_output(cmd, shell=True).rstrip().decode('ascii')
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell=True).rstrip().decode('ascii')
    cmd = "hostname | cut -d\' \' -f1"
    HOST = subprocess.check_output(cmd, shell=True).rstrip().decode('ascii')
    resolved = True
  except:
    pass
  finally:
    draw.text((x, top),   str(HOST), font=font, fill=255)
    draw.text((x, top+8),     str(SSID), font=font, fill=255)
    draw.text((x, top+16),  "IP: " + str(IP),  font=font, fill=255)
  disp.image(image)
  disp.display()

