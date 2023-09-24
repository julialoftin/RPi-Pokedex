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

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP

# API Request
pokemon_api_url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"

# Create an off-screen buffer
buffer = Image.new("1", (disp.width, disp.height))

# Define states
MENU_STATE = 0
POKEMON_LIST_STATE = 1

# Inititalize the current state and the selected menu item
current_state = MENU_STATE
selected_item = 1 # Initially selected Pokemon

# Create an off-screen buffer and drawing object for menu
buffer_menu = Image.new("1", (disp.width, disp.height))
draw_menu = ImageDraw.Draw(buffer_menu)

# Initialize a flag for menu content update
update_menu = True

while True:
    if current_state == MENU_STATE:
        if update_menu:
            # Display menu options
            disp.fill(0)
            disp.show()
            width = disp.width
            height = disp.height
            image = Image.new("1", (width, height))

            # Use the pre-created buffer and drawing object for menu
            draw = draw_menu
            draw.rectangle((0, 0, width, height), outline=0, fill=0)  # Clear the buffer

            draw.text((0, 0), "Menu:", fill=1)
        
            # Check which item is selected and add symbols
            if selected_item == 1:
                draw.text((0, 10), "# 1. Pokemon", fill=1)  # Add ● symbol for selection
                draw.text((0, 20), "2. Other Option", fill=1)
            else:
                draw.text((0, 10), "1. Pokemon", fill=1)
                draw.text((0, 20), "# 2. Other Option", fill=1)

            disp.image(buffer_menu)
            disp.show()
            update_menu = False

        # Check for button_A presses to change state
        if not button_A.value:
            current_state = POKEMON_LIST_STATE

    elif current_state == POKEMON_LIST_STATE:
        # Display list of pokemon
        try:
            # GET request
            response = requests.get(pokemon_api_url)

            # Check if request is successful
            if response.status_code == 200:
                # Parse JSON data
                pokemon_data = response.json().get("results", [])

                # Initialize variables for scrolling
                start_index = 0
                display_count = 6
                total_pokemon = len(pokemon_data)
                update_display = True

                # Create an off-screen buffer and drawing object for Pokemon list
                buffer_pokemon = Image.new("1", (disp.width, disp.height))
                draw_pokemon = ImageDraw.Draw(buffer_pokemon)

                while True:
                    if update_display:
                        # Clear the off-screen display
                        buffer_pokemon.paste(0, (0, 0, disp.width, disp.height))

                        # Create a drawing object
                        draw = draw_pokemon

                        # Display a subset of pokemon names
                        for i in range(start_index, min(start_index + display_count, total_pokemon)):
                            pokemon_name = pokemon_data[i].get("name", "")
                            draw.text((0, (i - start_index) * 10), pokemon_name, fill=1)

                        disp.image(buffer_pokemon)
                        disp.show()
                        update_display = False

                    # Button handling for scrolling
                    
                    if not button_U.value:
                        start_index = max(start_index - 1, 0)
                        update_display = True
                    elif not button_D.value:
                        if start_index < total_pokemon - display_count:
                            start_index += 1
                            update_display = True
                    elif not button_B.value:
                        current_state = MENU_STATE
                        update_menu = True
                        break        

                    time.sleep(0.2)

            else:
                print(f"Failed to fetch Pokémon data. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        