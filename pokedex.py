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


# Create an off-screen buffer and drawing object for Menu List
buffer_main_menu = Image.new("1", (disp.width, disp.height))
draw_main_menu = ImageDraw.Draw(buffer_main_menu)

# Define states
MAIN_MENU_STATE = 0

# Initialize the current state and the selected menu item
current_state = MAIN_MENU_STATE

# Initialize start index for scrolling
start_index_menu = 0

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
    return main_menu_items


while True:

    if current_state == MAIN_MENU_STATE:
        selected_index_main_menu = 0
        main_menu_items_length = len(update_display_main_menu(selected_index_main_menu))

        if not button_U.value:
            selected_index_main_menu = (selected_index_main_menu - 1) % main_menu_items_length # Scroll Down
            if selected_index_main_menu < 0:
                selected_index_main_menu = main_menu_items_length - 1

        # if selected_index_main_menu == 0:
        #     start_index_menu = 0
        #     update_display_main_menu(selected_index_main_menu)

        # if selected_index_main_menu == main_menu_items_length - 1:
        #     start_index_menu = main_menu_items_length - 3
        #     update_display_main_menu(selected_index_main_menu)