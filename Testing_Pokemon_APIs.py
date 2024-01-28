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
button_D.pull = Pull.UP

# API Requests
generations_api_url = "https://pokeapi.co/api/v2/generation"
generation_i_api_url = "https://pokeapi.co/api/v2/generation/1/"

# Create an off-screen buffer and drawing object for Menu List
buffer_menu = Image.new("1", (disp.width, disp.height))
draw_menu = ImageDraw.Draw(buffer_menu)

# Create an off-screen buffer and drawing object for Generation I List
buffer_generation_i_list = Image.new("1", (disp.width, disp.height))
draw_generation_i_list = ImageDraw.Draw(buffer_generation_i_list)

# Create an off-screen buffer and drawing object for Generation I Main Region List
buffer_generation_i_main_region = Image.new("1", (disp.width, disp.height))
draw_generation_i_main_region = ImageDraw.Draw(buffer_generation_i_main_region)

# Define states
MENU_STATE = 0
GENERATION_I_STATE = 2
GENERATION_I_MAIN_REGION_STATE = 11
GENERATION_II_STATE = 3
GENERATION_III_STATE = 4
GENERATION_IV_STATE = 5
GENERATION_V_STATE = 6
GENERATION_VI_STATE = 7
GENERATION_VII_STATE = 8
GENERATION_VIII_STATE = 9
GENERATION_IX_STATE = 10

# Initialize the current state and the selected menu item
current_state = MENU_STATE

# Initialize flags for menu and display updates
update_display = True

# Initialize start index for scrolling
start_index_menu = 0
start_index_generation_i = 0
start_index_generation_i_main_region = 0

def clear_buffer(buffer, draw):
    draw.rectangle((0, 0, buffer.width, buffer.height), outline=0, fill=0)

def update_menu_display(selected_menu_index):
    global start_index_menu

    clear_buffer(buffer_menu, draw_menu)
    draw_menu.text((0, 0), "Menu:", fill=1)

    display_count = 5
    max_visible_items = min(display_count, total_generations - start_index_menu)

    # Handle wrapping when reaching the end or beginning of the list
    if selected_menu_index < start_index_menu:
        start_index_menu = selected_menu_index
    elif selected_menu_index >= start_index_menu + max_visible_items:
        start_index_menu = selected_menu_index - max_visible_items + 1

    for i in range(max_visible_items):
        generation_name = generation_data[start_index_menu + i].get("name", "")
        display_text = f"{generation_name}"

        if i + start_index_menu == selected_menu_index:
            display_text = f"# {display_text}"

        draw_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_menu)
    disp.show()

def update_generation_i_display(selected_generation_i_index):
    clear_buffer(buffer_generation_i_list, draw_generation_i_list)

    # generation_i_items = ["Pokemon", "Types", "Moves"]
    generation_i_items = ["Main Region", "Moves", "Pokemon Species", "Types", "Versions"]

    for i, item in enumerate(generation_i_items):
        display_text = item

        if i == selected_generation_i_index:
            display_text = f"# {display_text}"

        draw_generation_i_list.text((0, (i * 10)), display_text, fill=1)

    disp.image(buffer_generation_i_list)
    disp.show()

def update_generation_i_main_region_display(selected_generation_i_main_region_index):
    clear_buffer(buffer_generation_i_main_region, draw_generation_i_main_region)

    display_count = 1

    max_visible_items = min(display_count, total_regions - start_index_generation_i_main_region)

    for i in range(max_visible_items):
        try:
            region_data = main_region_data
            region_name = region_data.get("name", "")
            display_text = f"{region_name}"

            if i + start_index_generation_i_main_region == selected_generation_i_main_region_index:
                display_text = f"# {display_text}"

            draw_generation_i_main_region.text((0, (i * 10) + 10), display_text, fill=1)
        except KeyError as e:
            print(f"KeyError: {e}, main_region_data: {main_region_data}")

    disp.image(buffer_generation_i_main_region)
    disp.show()

while True:
    if current_state == MENU_STATE:
        try:
            response = requests.get(generations_api_url)
            if response.status_code == 200:
                generation_data = response.json().get("results", [])
                total_generations = len(generation_data)
                selected_menu_index = 0
                while True:
                    if update_display:
                        update_menu_display(selected_menu_index)
                        update_display = False

                    if not button_U.value:
                        selected_menu_index = (
                            selected_menu_index - 1
                        ) % total_generations  # Scroll up
                        if selected_menu_index < start_index_menu:
                            start_index_menu = selected_menu_index
                        update_display = True
                        update_menu_display(selected_menu_index)

                    elif not button_D.value:
                        selected_menu_index = (
                            selected_menu_index + 1
                        ) % total_generations  # Scroll down
                        if selected_menu_index >= start_index_menu + 5:
                            start_index_menu = selected_menu_index - 4
                        update_display = True
                        update_menu_display(selected_menu_index)

                    if not button_A.value:
                        if selected_menu_index == 0:
                            current_state = GENERATION_I_STATE
                            update_display = True
                            break
            else:
                print(
                    f"Failed to fetch Generation data. Status code: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            print(f"An error occured: {e}")

    elif current_state == GENERATION_I_STATE:
        selected_generation_i_index = 0
        total_generation_i_items = 5

        update_generation_i_display(selected_generation_i_index)

        while True:
            if update_display:
                update_generation_i_display(selected_generation_i_index)
                update_display = False

            if not button_U.value:
                selected_generation_i_index = (
                    selected_generation_i_index - 1
                ) % total_generation_i_items  # Scroll down
                if selected_generation_i_index < 0:
                    selected_generation_i_index = total_generation_i_items - 1
                update_display = True

            elif not button_D.value:
                selected_generation_i_index = (
                    selected_generation_i_index + 1
                ) % total_generation_i_items  # Scroll down
                if selected_generation_i_index >= total_generation_i_items:
                    selected_generation_i_index = 0
                update_display = True

            elif not button_B.value:
                current_state = MENU_STATE
                update_display = True
                break

            if not button_A.value:
                if selected_generation_i_index == 0:
                    print(f"Selected Index: {selected_generation_i_index}")
                    try:
                        response = requests.get(generation_i_api_url)
                        if response.status_code == 200:
                            main_region_data = response.json().get("main_region", {}).get("name", "")
                            total_regions = len(main_region_data)
                            selected_generation_i_main_region_index = 0
                            current_state = GENERATION_I_MAIN_REGION_STATE
                            update_display = True
                            print("Transitioning to GENERATION_I_MAIN_REGION_STATE")
                        else:
                            print(f"Failed to fetch main region data. Status code: {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"An error occurred: {e}")

            # Looping display for end and beginning

            if selected_generation_i_index == 0:
                start_index_generation_i = 0
                update_generation_i_display(selected_generation_i_index)
                update_display = True

            if selected_generation_i_index == total_generation_i_items - 1:
                start_index_generation_i = total_generation_i_items - 3
                update_generation_i_display(selected_generation_i_index)
                update_display = True

            elif not button_A.value and selected_generation_i_index == 0:
                current_state = GENERATION_I_MAIN_REGION_STATE
                update_display = True
                break

    elif current_state == GENERATION_I_MAIN_REGION_STATE:
        print("In GENERATION_I_MAIN_REGION_STATE")
        try:
            response = requests.get(generation_i_api_url)

            if response.status_code == 200:
                main_region_data = response.json().get("main_region", [])
                total_regions = len(main_region_data)
                selected_generation_i_main_region_index = 0

                while True:
                    if update_display:
                        update_generation_i_main_region_display(selected_generation_i_main_region_index)
                        update_display = False

                    if not button_U.value:
                        selected_generation_i_main_region_index = (
                            selected_generation_i_main_region_index - 1
                        ) % total_regions  # Scroll down
                        if selected_generation_i_main_region_index < 0:
                            selected_generation_i_main_region_index = total_regions - 1
                        update_display = True

                    elif not button_D.value:
                        selected_generation_i_main_region_index = (
                            selected_generation_i_main_region_index + 1
                        ) % total_regions  # Scroll down
                        if selected_generation_i_main_region_index >= total_regions:
                            selected_generation_i_main_region_index = 0
                        update_display = True

                    elif not button_B.value:
                        current_state = GENERATION_I_STATE
                        update_display = True
                        break

            else:
                print(
                    f"Failed to fetch Pokémon data. Status code: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")