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

# API URLs


# Create an off-screen buffer and drawing object for Main Menu List
buffer_main_menu = Image.new("1", (disp.width, disp.height))
draw_main_menu = ImageDraw.Draw(buffer_main_menu)
# Create an off-screen buffer and drawing object for Generations Menu List
buffer_generations_menu = Image.new("1", (disp.width, disp.height))
draw_generations_menu = ImageDraw.Draw(buffer_generations_menu)

# Define states
MAIN_MENU_STATE = 0
GENERATIONS_MENU_STATE = 1

# Initialize the current state and the selected menu item
current_state = MAIN_MENU_STATE

# Initialize start index for scrolling
start_index_menu = 0
start_index_generations_menu = 0

def clear_buffer(buffer, draw):
    draw.rectangle((0, 0, buffer.width, buffer.height), outline=0, fill=0)

def update_display_main_menu(selected_index_main_menu):
    clear_buffer(buffer_main_menu, draw_main_menu)
    draw_main_menu.text((0, 0), "PokeDictionary", fill=1)

    main_menu_items = ["Generations", "Items", "Pokemon"]

    for i, item in enumerate(main_menu_items):
        display_text = item

        if i + start_index_menu == selected_index_main_menu:
            display_text = f"# {display_text}"

        draw_main_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_main_menu)
    disp.show()

def fetch_generation_data():
    try:
        response = requests.get("https://pokeapi.co/api/v2/generation")
        if response.status_code == 200:
            generation_data = response.json().get("results", [])
            return generation_data
        else:
            print(f"Failed to get Generations data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")


def update_display_generations_menu(selected_index_generations_menu):
    clear_buffer(buffer_generations_menu, draw_generations_menu)
    draw_generations_menu.text((0, 0), "Generations:", fill=1)

    display_count = 5
    total_generations_menu_items = len(fetch_generation_data())
    start_index_generations_menu = 0
    max_visible_items = min(display_count, total_generations_menu_items - start_index_generations_menu)

    generation_results = fetch_generation_data()

    # Handle wrapping when reaching beginning and end of buffer display
    if selected_index_generations_menu < start_index_generations_menu:
        start_index_generations_menu = selected_index_generations_menu
    elif selected_index_generations_menu >=  start_index_generations_menu + max_visible_items:
        start_index_generations_menu = selected_index_generations_menu - max_visible_items + 1

    for i in range(max_visible_items):
        if start_index_generations_menu + i < total_generations_menu_items:
            generation_name = generation_results[start_index_generations_menu + i].get("name", "")
            display_text = f"{generation_name}"

            if i == selected_index_generations_menu:
                display_text = f"# {display_text}"

            draw_generations_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generations_menu)
    disp.show()


while True:

    if current_state == MAIN_MENU_STATE:
        selected_index_main_menu = 0
        total_main_menu_items = 3
        update_display_main_menu(selected_index_main_menu)

        selected_index_generations_menu = 0

        while True:
            update_display_main_menu(selected_index_main_menu)
            if not button_U.value:
                print("Button U Pressed")
                selected_index_main_menu = (selected_index_main_menu - 1) % total_main_menu_items
                if selected_index_main_menu < 0:
                    selected_index_main_menu = total_main_menu_items - 1
                update_display_main_menu(selected_index_main_menu)
            if not button_D.value:
                print("Button D Pressed")
                selected_index_main_menu = (selected_index_main_menu + 1) % total_main_menu_items
                if selected_index_main_menu >= total_main_menu_items:
                    selected_index_main_menu = 0
                update_display_main_menu(selected_index_main_menu)
            if not button_A.value:
                print("Button A Pressed")
                if selected_index_main_menu == 0:
                    current_state = GENERATIONS_MENU_STATE
                    break

    elif current_state == GENERATIONS_MENU_STATE:
        selected_index_generations_menu = 0
        total_generations_menu_items = len(fetch_generation_data())
        update_display_generations_menu(selected_index_generations_menu)

        while True:
            update_display_generations_menu(selected_index_generations_menu)
            if not button_U.value:
                print("Button U Pressed")
                selected_index_generations_menu = (selected_index_generations_menu - 1) % total_generations_menu_items
                if selected_index_generations_menu < 0:
                    selected_index_generations_menu = total_generations_menu_items - 1
                update_display_generations_menu(selected_index_generations_menu)
            if not button_D.value:
                print("Button D Pressed")
                selected_index_generations_menu = (selected_index_generations_menu + 1) % total_generations_menu_items
                if selected_index_generations_menu >= total_generations_menu_items:
                    selected_index_generations_menu = 0
                update_display_generations_menu(selected_index_generations_menu)

        

