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

# Create an off-screen buffer and drawing object for Generation I Moves List
buffer_generation_i_moves = Image.new("1", (disp.width, disp.height))
draw_generation_i_moves = ImageDraw.Draw(buffer_generation_i_moves)

# Create an off-screen buffer and drawing object for Generation I Pokemon Species List
buffer_generation_i_pokemon_species = Image.new("1", (disp.width, disp.height))
draw_generation_i_pokemon_species = ImageDraw.Draw(buffer_generation_i_pokemon_species)

# Define states
MENU_STATE = 0
GENERATION_I_STATE = 2
GENERATION_I_MAIN_REGION_STATE = 11
GENERATION_I_MOVES_STATE = 12
GENERATION_I_POKEMON_SPECIES_STATE = 13
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
start_index_generation_i_moves = 0
start_index_generation_i_pokemon_species = 0

total_regions = 0
selected_generation_i_main_region_index = 0
main_region_data = []

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

    generation_i_items = ["Main Region", "Moves", "Pokemon Species", "Types", "Versions"]

    for i, item in enumerate(generation_i_items):
        display_text = item

        if i == selected_generation_i_index:
            display_text = f"# {display_text}"

        draw_generation_i_list.text((0, (i * 10)), display_text, fill=1)

    disp.image(buffer_generation_i_list)
    disp.show()

def update_generation_i_main_region_display(selected_generation_i_main_region_index):
    global start_index_generation_i_main_region
    clear_buffer(buffer_generation_i_main_region, draw_generation_i_main_region)

    display_count = 1

    max_visible_items = min(display_count, total_regions - start_index_generation_i_main_region)

    for i in range(max_visible_items):
        try:
            region_data = main_region_data[start_index_generation_i_main_region + i]
            region_name = region_data.get("name", "")
            display_text = f"{region_name}"

            if i + start_index_generation_i_main_region == selected_generation_i_main_region_index:
                display_text = f"# {display_text}"

            draw_generation_i_main_region.text((0, (i * 10) + 10), display_text, fill=1)
        except KeyError as e:
            print(f"KeyError: {e}, main_region_data: {main_region_data}")

    disp.image(buffer_generation_i_main_region)
    disp.show()

def update_generation_i_moves_display(selected_generation_i_moves_index):
    global start_index_generation_i_moves
    clear_buffer(buffer_generation_i_moves, draw_generation_i_moves)
    draw_generation_i_moves.text((0, 0), "Moves:", fill=1)

    display_count = 5
    max_visible_items = min(display_count, total_moves - start_index_generation_i_moves)

    # Handle wrapping when reaching the end or beginning of the list
    if selected_generation_i_moves_index < start_index_generation_i_moves:
        start_index_generation_i_moves = selected_generation_i_moves_index
    elif selected_generation_i_moves_index >= start_index_generation_i_moves + max_visible_items:
        start_index_generation_i_moves = selected_generation_i_moves_index - max_visible_items + 1

    for i in range(max_visible_items):
        try:
            move_data = moves_data[start_index_generation_i_moves + i]
            move_name = move_data.get("name", "")
            display_text = f"{move_name}"

            if i + start_index_generation_i_moves == selected_generation_i_moves_index:
                display_text = f"# {display_text}"

            draw_generation_i_moves.text((0, (i * 10) + 10), display_text, fill=1)
        except KeyError as e:
            print(f"KeyError: {e}, moves_data: {moves_data}")

    disp.image(buffer_generation_i_moves)
    disp.show()

def update_generation_i_pokemon_species_display(selected_generation_i_pokemon_species_index):
    global start_index_generation_i_pokemon_species
    clear_buffer(buffer_generation_i_pokemon_species, draw_generation_i_pokemon_species)
    draw_generation_i_pokemon_species.text((0, 0), "Pokemon:", fill=1)

    display_count = 5
    max_visible_items = min(display_count, total_pokemon_species - start_index_generation_i_pokemon_species)

    # Handle wrapping when reaching the end or beginning of the list
    if selected_generation_i_pokemon_species_index < start_index_generation_i_pokemon_species:
        start_index_generation_i_pokemon_species = selected_generation_i_pokemon_species_index
    elif selected_generation_i_pokemon_species_index >= start_index_generation_i_pokemon_species + max_visible_items:
        start_index_generation_i_pokemon_species = selected_generation_i_pokemon_species_index - max_visible_items + 1

    for i in range(max_visible_items):
        try:
            pokemon_species_data = pokemon_species_data[start_index_generation_i_pokemon_species + i]
            pokemon_species_name = pokemon_species_data.get("name", "")
            display_text = f"# {display_text}"

            if i + start_index_generation_i_pokemon_species == selected_generation_i_pokemon_species_index:
                display_text = f"# {display_text}"

            draw_generation_i_pokemon_species.text((0, (i * 10) + 10), display_text, fill=1)
        except KeyError as e:
            print(f"KeyError: {e}, pokemon_species_data: {pokemon_species_data}")

    disp.image(buffer_generation_i_pokemon_species)
    disp.show()

def fetch_generation_i_main_region():
    global total_regions, main_region_data, selected_generation_i_main_region_index, current_state, update_display
    try:
        response = requests.get(generation_i_api_url)
        if response.status_code == 200:
            data = response.json()
            main_region_data = [data["main_region"]]
            total_regions = len(main_region_data)
            selected_generation_i_main_region_index = 0
            current_state = GENERATION_I_MAIN_REGION_STATE
            update_display = True
            print("Transitioning to GENERATION_I_MAIN_REGION_STATE")
            return total_regions
        else:
            print(f"Failed to fetch main region data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_generation_1_moves():
    global moves_data, total_moves, selected_generation_i_moves_index, current_state, update_display
    try:
        response = requests.get(generation_i_api_url)
        if response.status_code == 200:
            moves_data = response.json().get("moves", [])
            if moves_data:
                total_moves = len(moves_data)
                selected_generation_i_moves_index = 0
                current_state = GENERATION_I_MOVES_STATE
                update_display = True
                print(f"Transitioning to GENERATION_I_MOVES_STATE")
                return total_moves
            else:
                print(f"Moves data is empty.")
        else:
            print(f"Failed to fetch moves data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_generation_1_pokemon_species():
    global pokemon_species_data, total_pokemon_species, selected_generation_i_pokemon_species_index, current_state, update_display
    try:
        response = requests.get(generation_i_api_url)
        if response.status_code == 200:
            pokemon_species_data = response.json().get("pokemon_species", [])
            if pokemon_species_data:
                total_pokemon_species = len(pokemon_species_data)
                selected_generation_i_pokemon_species_index = 0
                current_state = GENERATION_I_POKEMON_SPECIES_STATE
                update_display = True
                print(f"Transitioning to GENERATION_I_POKEMON_SPECIES_STATE")
                return total_pokemon_species
            else:
                print(f"Pokemon species is empty.")
        else:
            print(f"Failed to fetch pokemon species data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print (f"An error occurred: {e}")

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
        selected_generation_i_moves_index = 0
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
                    fetch_generation_i_main_region()
                elif selected_generation_i_index == 1:
                    print(f"Selected Index: {selected_generation_i_index}")
                    fetch_generation_1_moves()

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

            elif not button_A.value and selected_generation_i_moves_index == 0:
                current_state = GENERATION_I_MOVES_STATE
                update_display = True
                break

    elif current_state == GENERATION_I_MAIN_REGION_STATE:
        print("In GENERATION_I_MAIN_REGION_STATE")
        selected_generation_i_main_region_index = 0
        total_regions = fetch_generation_i_main_region()
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

    elif current_state == GENERATION_I_MOVES_STATE:
        print(f"In GENERATION_I_MOVES_STATE")
        selected_generation_i_moves_index = 0
        total_moves = fetch_generation_1_moves()

        while True:
            if update_display:
                update_generation_i_moves_display(selected_generation_i_moves_index)
                update_display = False

            if not button_U.value:
                selected_generation_i_moves_index = (
                    selected_generation_i_moves_index - 1
                ) % total_moves # Scroll up
                if selected_generation_i_moves_index < 0:
                    selected_generation_i_moves_index = total_moves - 1
                update_display = True

            elif not button_D.value:
                selected_generation_i_moves_index = (
                    selected_generation_i_moves_index + 1
                ) % total_moves # Scroll down
                if selected_generation_i_moves_index >= total_moves:
                    selected_generation_i_moves_index = 0
                update_display = True

            elif not button_B.value:
                current_state = GENERATION_I_STATE
                update_display = True
                break
    
    elif current_state == GENERATION_I_POKEMON_SPECIES_STATE:
        print(f"In GENERATION_I_POKEMON_SPECIES_STATE")
        selected_generation_i_pokemon_species_index = 0
        total_pokemon_species = fetch_generation_1_pokemon_species()

        while True:
            if update_display:
                update_generation_i_pokemon_species_display(selected_generation_i_pokemon_species_index)
                update_display = False

            if not button_U.value:
                selected_generation_i_pokemon_species_index = (
                    selected_generation_i_pokemon_species_index - 1
                ) % total_pokemon_species # Scroll up
                if selected_generation_i_pokemon_species_index < 0:
                    selected_generation_i_pokemon_species_index = total_pokemon_species - 1
                update_display = True

            elif not button_D.value:
                selected_generation_i_pokemon_species_index = (
                    selected_generation_i_pokemon_species_index + 1
                ) % total_pokemon_species # Scroll down
                if selected_generation_i_pokemon_species_index >= total_pokemon_species:
                    selected_generation_i_pokemon_species_index = 0
                update_display = True

            elif not button_B.value:
                current_state = GENERATION_I_STATE
                update_display = True
                break
