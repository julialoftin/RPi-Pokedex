""" Sets up Pi display and buttons """

import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import requests

# Creates the i2c interface
i2c = busio.I2C(board.SCL, board.SDA)

# Creates the SSD1306 OLED class
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


def clear_buffer(buffer, draw):
    """Clears screen for drawing"""
    draw.rectangle((0, 0, buffer.width, buffer.height), outline=0, fill=0)


# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

# Create an off-screen buffer and drawing object for Main Menu
buffer_main_menu = Image.new("1", (disp.width, disp.height))
draw_main_menu = ImageDraw.Draw(buffer_main_menu)
# Create an off-screen buffer and drawing object for Generations Menu
buffer_generations_menu = Image.new("1", (disp.width, disp.height))
draw_generations_menu = ImageDraw.Draw(buffer_generations_menu)
# Create an off-screen buffer and drawing object for Generation I Menu
buffer_generation_i_menu = Image.new("1", (disp.width, disp.height))
draw_generation_i_menu = ImageDraw.Draw(buffer_generation_i_menu)
# Create an off-screen buffer and drawing object for Generation II Menu
buffer_generation_ii_menu = Image.new("1", (disp.width, disp.height))
draw_generation_ii_menu = ImageDraw.Draw(buffer_generation_ii_menu)
# Create an off-screen buffer and drawing object for Generation III Menu
buffer_generation_iii_menu = Image.new("1", (disp.width, disp.height))
draw_generation_iii_menu = ImageDraw.Draw(buffer_generation_iii_menu)
# Create an off-screen buffer and drawing object for Generation IV Menu
buffer_generation_iv_menu = Image.new("1", (disp.width, disp.height))
draw_generation_iv_menu = ImageDraw.Draw(buffer_generation_iv_menu)
# Create an off-screen buffer and drawing object for Generation V Menu
buffer_generation_v_menu = Image.new("1", (disp.width, disp.height))
draw_generation_v_menu = ImageDraw.Draw(buffer_generation_v_menu)
# Create an off-screen buffer and drawing object for Generation VI Menu
buffer_generation_vi_menu = Image.new("1", (disp.width, disp.height))
draw_generation_vi_menu = ImageDraw.Draw(buffer_generation_vi_menu)
# Create an off-screen buffer and drawing object for Generation VII Menu
buffer_generation_vii_menu = Image.new("1", (disp.width, disp.height))
draw_generation_vii_menu = ImageDraw.Draw(buffer_generation_vii_menu)
# Create an off-screen buffer and drawing object for Generation VIII Menu
buffer_generation_viii_menu = Image.new("1", (disp.width, disp.height))
draw_generation_viii_menu = ImageDraw.Draw(buffer_generation_viii_menu)
# Create an off-screen buffer and drawing object for Generation IX Menu
buffer_generation_ix_menu = Image.new("1", (disp.width, disp.height))
draw_generation_ix_menu = ImageDraw.Draw(buffer_generation_ix_menu)

# Create an off-screen buffer and drawing object for Generation I Main Region Menu
buffer_generation_i_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_i_main_region_menu = ImageDraw.Draw(
    buffer_generation_i_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation II Main Region Menu
buffer_generation_ii_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_ii_main_region_menu = ImageDraw.Draw(
    buffer_generation_ii_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation III Main Region Menu
buffer_generation_iii_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_iii_main_region_menu = ImageDraw.Draw(
    buffer_generation_iii_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation IV Main Region Menu
buffer_generation_iv_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_iv_main_region_menu = ImageDraw.Draw(
    buffer_generation_iv_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation V Main Region Menu
buffer_generation_v_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_v_main_region_menu = ImageDraw.Draw(
    buffer_generation_v_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation VI Main Region Menu
buffer_generation_vi_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_vi_main_region_menu = ImageDraw.Draw(
    buffer_generation_vi_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation VII Main Region Menu
buffer_generation_vii_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_vii_main_region_menu = ImageDraw.Draw(
    buffer_generation_vii_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation VIII Main Region Menu
buffer_generation_viii_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_viii_main_region_menu = ImageDraw.Draw(
    buffer_generation_viii_main_region_menu
)
# Create an off-screen buffer and drawing object for Generation IX Main Region Menu
buffer_generation_ix_main_region_menu = Image.new("1", (disp.width, disp.height))
draw_generation_ix_main_region_menu = ImageDraw.Draw(
    buffer_generation_ix_main_region_menu
)

# Create an off-screen buffer and drawing object for Generation I Moves Menu
buffer_generation_i_moves_menu = Image.new("1", (disp.width, disp.height))
draw_generation_i_moves_menu = ImageDraw.Draw(buffer_generation_i_moves_menu)
