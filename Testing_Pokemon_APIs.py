import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
import requests

# Creates the i2c interface
i2c = busio.I2C(board.SCL, board.SDA)

# Creates the SSD1306 OLED class
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

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
button_D.pull = Pull.U

# API Requests
pokemon_api_url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
generations_api_url = "https://pokeapi.co/api/v2/generation"
generation_i_api_url = "https://pokeapi.co/api/v2/generation/1/"

def create_buffer_and_draw():
    buffer = Image.new("1", (disp.width, disp.height))
    draw = ImageDraw.Draw(buffer)
    return buffer, draw

def clear_buffer(buffer, draw):
    draw.rectangle((0, 0, buffer.width, buffer.height), outline=0, fill=0)

# Define states
MAIN_MENU_STATE = 0
GENERATIONS_MENU_STATE = 1
POKEMON_LIST_STATE = 2
POKEMON_DETAILS_STATE = 3

current_state = MAIN_MENU_STATE
update_display = True

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json().get("results", [])
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return []

        