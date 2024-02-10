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
GENERATION_API_URL = "https://pokeapi.co/api/v2/generation"

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

# Define states
MAIN_MENU_STATE = 0
GENERATIONS_MENU_STATE = 1
GENERATION_I_MENU_STATE = 2
GENERATION_II_MENU_STATE = 3
GENERATION_III_MENU_STATE = 4
GENERATION_IV_MENU_STATE = 5
GENERATION_V_MENU_STATE = 6
GENERATION_VI_MENU_STATE = 7
GENERATION_VII_MENU_STATE = 8
GENERATION_VIII_MENU_STATE = 9
GENERATION_IX_MENU_STATE = 10

GENERATION_I_MAIN_REGION_MENU_STATE = 11
GENERATION_II_MAIN_REGION_MENU_STATE = 12
GENERATION_III_MAIN_REGION_MENU_STATE = 13
GENERATION_IV_MAIN_REGION_MENU_STATE = 14
GENERATION_V_MAIN_REGION_MENU_STATE = 15
GENERATION_VI_MAIN_REGION_MENU_STATE = 16
GENERATION_VII_MAIN_REGION_MENU_STATE = 17
GENERATION_VIII_MAIN_REGION_MENU_STATE = 18
GENERATION_IX_MAIN_REGION_MENU_STATE = 19

GENERATION_I_MOVES_MENU_STATE = 20

# Initialize the current state and the selected menu item
CURRENT_STATE = MAIN_MENU_STATE

# Initialize start index for scrolling
START_INDEX_MENU = 0
START_INDEX_GENERATIONS_MENU = 0
START_INDEX_GENERATION_I_MENU = 0
START_INDEX_GENERATION_II_MENU = 0
START_INDEX_GENERATION_III_MENU = 0
START_INDEX_GENERATION_IV_MENU = 0
START_INDEX_GENERATION_V_MENU = 0
START_INDEX_GENERATION_VI_MENU = 0
START_INDEX_GENERATION_VII_MENU = 0
START_INDEX_GENERATION_VIII_MENU = 0
START_INDEX_GENERATION_IX_MENU = 0

START_INDEX_GENERATION_I_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_II_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_III_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_IV_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_V_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_VI_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_VII_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_VIII_MAIN_REGION_MENU = 0
START_INDEX_GENERATION_IX_MAIN_REGION_MENU = 0

START_INDEX_GENERATION_I_MOVES_MENU = 0


def clear_buffer(buffer, draw):
    """Clears screen for drawing"""
    draw.rectangle((0, 0, buffer.width, buffer.height), outline=0, fill=0)


def update_display_main_menu(selected_index):
    """Creates main display menu"""
    clear_buffer(buffer_main_menu, draw_main_menu)
    draw_main_menu.text((0, 0), "PokeDictionary", fill=1)

    main_menu_items = ["Generations", "Items", "Pokemon"]

    for i, item in enumerate(main_menu_items):
        display_text = item

        if i + START_INDEX_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_main_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_main_menu)
    disp.show()


def fetch_generation_data():
    """Calls API for generation data"""
    try:
        response = requests.get(GENERATION_API_URL)
        if response.status_code == 200:
            generation_data = response.json().get("results", [])
            return generation_data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_i_data():
    """Calls API for generation 1 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/1/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_ii_data():
    """Calls API for generation 2 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/2/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_iii_data():
    """Calls API for generation 3 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/3/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_iv_data():
    """Calls API for generation 4 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/4/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_v_data():
    """Calls API for generation 5 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/5/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_vi_data():
    """Calls API for generation 6 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/6/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_vii_data():
    """Calls API for generation 7 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/7/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_viii_data():
    """Calls API for generation 8 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/8/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_ix_data():
    """Calls API for generation 9 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/9/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def update_display_generations_menu(selected_index):
    """Creates generations menu display"""
    clear_buffer(buffer_generations_menu, draw_generations_menu)
    draw_generations_menu.text((0, 0), "Generations:", fill=1)

    display_count = 5
    # total_generations_menu_items = len(fetch_generation_data())
    start_index_generations_menu = 0
    max_visible_items = min(
        display_count, total_generations_menu_items - start_index_generations_menu
    )

    generation_results = fetch_generation_data()

    # Handle wrapping when reaching beginning and end of buffer display
    if selected_index < start_index_generations_menu:
        start_index_generations_menu = selected_index
    elif selected_index >= start_index_generations_menu + max_visible_items:
        start_index_generations_menu = selected_index - max_visible_items + 1

    for i in range(max_visible_items):
        if start_index_generations_menu + i < total_generations_menu_items:
            generation_name = generation_results[start_index_generations_menu + i].get(
                "name", ""
            )
            display_text = f"{generation_name}"

            if start_index_generations_menu + i == selected_index:
                display_text = f"# {display_text}"

            draw_generations_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generations_menu)
    disp.show()


def update_display_generation_i_menu(selected_index):
    """Creates generation 1 menu display"""
    clear_buffer(buffer_generation_i_menu, draw_generation_i_menu)
    draw_generation_i_menu.text((0, 0), "Generation I:", fill=1)

    generation_i_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_i_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_I_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_i_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_i_menu)
    disp.show()


def update_display_generation_ii_menu(selected_index):
    """Creates generation 2 menu display"""
    clear_buffer(buffer_generation_ii_menu, draw_generation_ii_menu)
    draw_generation_ii_menu.text((0, 0), "Generation II:", fill=1)

    generation_ii_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_ii_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_II_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_ii_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_ii_menu)
    disp.show()


def update_display_generation_iii_menu(selected_index):
    """Creates generation 3 menu display"""
    clear_buffer(buffer_generation_iii_menu, draw_generation_iii_menu)
    draw_generation_iii_menu.text((0, 0), "Generation III:", fill=1)

    generation_iii_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_iii_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_III_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_iii_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_iii_menu)
    disp.show()


def update_display_generation_iv_menu(selected_index):
    """Creates generation 4 menu display"""
    clear_buffer(buffer_generation_iv_menu, draw_generation_iv_menu)
    draw_generation_iv_menu.text((0, 0), "Generation IV:", fill=1)

    generation_iv_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_iv_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_IV_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_iv_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_iv_menu)
    disp.show()


def update_display_generation_v_menu(selected_index):
    """Creates generation 5 menu display"""
    clear_buffer(buffer_generation_v_menu, draw_generation_v_menu)
    draw_generation_v_menu.text((0, 0), "Generation V:", fill=1)

    generation_v_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_v_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_V_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_v_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_v_menu)
    disp.show()


def update_display_generation_vi_menu(selected_index):
    """Creates generation 6 menu display"""
    clear_buffer(buffer_generation_vi_menu, draw_generation_vi_menu)
    draw_generation_vi_menu.text((0, 0), "Generation VI:", fill=1)

    generation_vi_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_vi_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_VI_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_vi_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_vi_menu)
    disp.show()


def update_display_generation_vii_menu(selected_index):
    """Creates generation 7 menu display"""
    clear_buffer(buffer_generation_vii_menu, draw_generation_vii_menu)
    draw_generation_vii_menu.text((0, 0), "Generation VII:", fill=1)

    generation_vii_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_vii_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_VII_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_vii_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_vii_menu)
    disp.show()


def update_display_generation_viii_menu(selected_index):
    """Creates generation 8 menu display"""
    clear_buffer(buffer_generation_viii_menu, draw_generation_viii_menu)
    draw_generation_viii_menu.text((0, 0), "Generation VIII:", fill=1)

    generation_viii_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_viii_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_VIII_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_viii_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_viii_menu)
    disp.show()


def update_display_generation_ix_menu(selected_index):
    """Creates generation 9 menu display"""
    clear_buffer(buffer_generation_ix_menu, draw_generation_ix_menu)
    draw_generation_ix_menu.text((0, 0), "Generation IX:", fill=1)

    generation_ix_menu_items = [
        "Main Region",
        "Moves",
        "Pokemon Species",
        "Pokemon Types",
        "Game Versions",
    ]

    for i, item in enumerate(generation_ix_menu_items):
        display_text = item

        if i + START_INDEX_GENERATION_IX_MENU == selected_index:
            display_text = f"# {display_text}"

        draw_generation_ix_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_ix_menu)
    disp.show()


def update_display_generation_i_main_region_menu(selected_index):
    """Creates generation 1 main region menu display"""
    clear_buffer(
        buffer_generation_i_main_region_menu, draw_generation_i_main_region_menu
    )
    draw_generation_i_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_i_main_region_menu_items = len(main_region_data)
    start_index_generation_i_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_i_main_region_menu_items
        - start_index_generation_i_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_i_main_region_menu + i
            < total_generation_i_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_i_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_i_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_i_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_i_main_region_menu)
    disp.show()


def update_display_generation_ii_main_region_menu(selected_index):
    """Creates generation 2 main region menu display"""
    clear_buffer(
        buffer_generation_ii_main_region_menu, draw_generation_ii_main_region_menu
    )
    draw_generation_ii_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_ii_main_region_menu_items = len(main_region_data)
    start_index_generation_ii_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_ii_main_region_menu_items
        - start_index_generation_ii_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_ii_main_region_menu + i
            < total_generation_ii_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_ii_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_ii_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_ii_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_ii_main_region_menu)
    disp.show()


def update_display_generation_iii_main_region_menu(selected_index):
    """Creates generation 3 main region menu display"""
    clear_buffer(
        buffer_generation_iii_main_region_menu, draw_generation_iii_main_region_menu
    )
    draw_generation_iii_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_iii_main_region_menu_items = len(main_region_data)
    start_index_generation_iii_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_iii_main_region_menu_items
        - start_index_generation_iii_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_iii_main_region_menu + i
            < total_generation_iii_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_iii_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_iii_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_iii_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_iii_main_region_menu)
    disp.show()


def update_display_generation_iv_main_region_menu(selected_index):
    """Creates generation 4 main region menu display"""
    clear_buffer(
        buffer_generation_iv_main_region_menu, draw_generation_iv_main_region_menu
    )
    draw_generation_iv_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_iv_main_region_menu_items = len(main_region_data)
    start_index_generation_iv_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_iv_main_region_menu_items
        - start_index_generation_iv_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_iv_main_region_menu + i
            < total_generation_iv_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_iv_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_iv_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_iv_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_iv_main_region_menu)
    disp.show()


def update_display_generation_v_main_region_menu(selected_index):
    """Creates generation 5 main region menu display"""
    clear_buffer(
        buffer_generation_v_main_region_menu, draw_generation_v_main_region_menu
    )
    draw_generation_v_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_v_main_region_menu_items = len(main_region_data)
    start_index_generation_v_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_v_main_region_menu_items
        - start_index_generation_v_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_v_main_region_menu + i
            < total_generation_v_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_v_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_v_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_v_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_v_main_region_menu)
    disp.show()


def update_display_generation_vi_main_region_menu(selected_index):
    """Creates generation 6 main region menu display"""
    clear_buffer(
        buffer_generation_vi_main_region_menu, draw_generation_vi_main_region_menu
    )
    draw_generation_vi_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_vi_main_region_menu_items = len(main_region_data)
    start_index_generation_vi_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_vi_main_region_menu_items
        - start_index_generation_vi_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_vi_main_region_menu + i
            < total_generation_vi_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_vi_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_vi_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_vi_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_vi_main_region_menu)
    disp.show()


def update_display_generation_vii_main_region_menu(selected_index):
    """Creates generation 7 main region menu display"""
    clear_buffer(
        buffer_generation_vii_main_region_menu, draw_generation_vii_main_region_menu
    )
    draw_generation_vii_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_vii_main_region_menu_items = len(main_region_data)
    start_index_generation_vii_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_vii_main_region_menu_items
        - start_index_generation_vii_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_vii_main_region_menu + i
            < total_generation_vii_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_vii_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_vii_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_vii_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_vii_main_region_menu)
    disp.show()


def update_display_generation_viii_main_region_menu(selected_index):
    """Creates generation 8 main region menu display"""
    clear_buffer(
        buffer_generation_viii_main_region_menu, draw_generation_viii_main_region_menu
    )
    draw_generation_viii_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_viii_main_region_menu_items = len(main_region_data)
    start_index_generation_viii_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_viii_main_region_menu_items
        - start_index_generation_viii_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_viii_main_region_menu + i
            < total_generation_viii_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_viii_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_viii_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_viii_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_viii_main_region_menu)
    disp.show()


def update_display_generation_ix_main_region_menu(selected_index):
    """Creates generation 9 main region menu display"""
    clear_buffer(
        buffer_generation_ix_main_region_menu, draw_generation_ix_main_region_menu
    )
    draw_generation_ix_main_region_menu.text((0, 0), "Main Regions:", fill=1)

    display_count = 5
    total_generation_ix_main_region_menu_items = len(main_region_data)
    start_index_generation_ix_main_region_menu = 0
    max_visible_items = min(
        display_count,
        total_generation_ix_main_region_menu_items
        - start_index_generation_ix_main_region_menu,
    )

    for i in range(max_visible_items):
        if (
            start_index_generation_ix_main_region_menu + i
            < total_generation_ix_main_region_menu_items
        ):
            region_name = main_region_data[
                start_index_generation_ix_main_region_menu + i
            ].get("name", "")

            display_text = f"{region_name}"

            if i + start_index_generation_ix_main_region_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_ix_main_region_menu.text(
                (0, (i * 10) + 10), display_text, fill=1
            )

    disp.image(buffer_generation_ix_main_region_menu)
    disp.show()


def update_display_generation_i_moves_menu(selected_index):
    """Creates generation 1 moves menu display"""
    clear_buffer(buffer_generation_i_moves_menu, draw_generation_i_moves_menu)
    draw_generation_i_moves_menu.text((0, 0), "Moves:", fill=1)

    display_count = 5
    start_index_generation_i_moves_menu = 0
    max_visible_items = min(
        display_count,
        TOTAL_GENERATION_I_MENU_ITEMS - start_index_generation_i_moves_menu,
    )

    # Handle wrapping when reaching beginning and end of buffer display
    if selected_index < start_index_generation_i_moves_menu:
        start_index_generation_i_moves_menu = selected_index
    elif selected_index >= start_index_generation_i_moves_menu + max_visible_items:
        start_index_generation_i_moves_menu = selected_index - max_visible_items + 1

    for i in range(max_visible_items):
        if (
            start_index_generation_i_moves_menu + i
            < total_generation_i_moves_menu_items
        ):
            move_name = moves_data[start_index_generation_i_moves_menu + i].get(
                "name", ""
            )

            display_text = f"{move_name}"

            if i + start_index_generation_i_moves_menu == selected_index:
                display_text = f"# {display_text}"

            draw_generation_i_moves_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_i_moves_menu)
    disp.show()


while True:

    if CURRENT_STATE == MAIN_MENU_STATE:
        SELECTED_INDEX_MAIN_MENU = 0
        TOTAL_MAIN_MENU_ITEMS = 3
        update_display_main_menu(SELECTED_INDEX_MAIN_MENU)

        while True:
            update_display_main_menu(SELECTED_INDEX_MAIN_MENU)
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_MAIN_MENU = (
                    SELECTED_INDEX_MAIN_MENU - 1
                ) % TOTAL_MAIN_MENU_ITEMS
                if SELECTED_INDEX_MAIN_MENU < 0:
                    SELECTED_INDEX_MAIN_MENU = TOTAL_MAIN_MENU_ITEMS - 1
                update_display_main_menu(SELECTED_INDEX_MAIN_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_MAIN_MENU = (
                    SELECTED_INDEX_MAIN_MENU + 1
                ) % TOTAL_MAIN_MENU_ITEMS
                if SELECTED_INDEX_MAIN_MENU >= TOTAL_MAIN_MENU_ITEMS:
                    SELECTED_INDEX_MAIN_MENU = 0
                update_display_main_menu(SELECTED_INDEX_MAIN_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_MAIN_MENU == 0:
                    CURRENT_STATE = GENERATIONS_MENU_STATE
                    break

    if CURRENT_STATE == GENERATIONS_MENU_STATE:
        SELECTED_INDEX_GENERATIONS_MENU = 0
        total_generations_menu_items = len(fetch_generation_data())
        update_display_generations_menu(SELECTED_INDEX_GENERATIONS_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATIONS_MENU = (
                    SELECTED_INDEX_GENERATIONS_MENU - 1
                ) % total_generations_menu_items
                if SELECTED_INDEX_GENERATIONS_MENU < 0:
                    SELECTED_INDEX_GENERATIONS_MENU = total_generations_menu_items - 1
                update_display_generations_menu(SELECTED_INDEX_GENERATIONS_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATIONS_MENU = (
                    SELECTED_INDEX_GENERATIONS_MENU + 1
                ) % total_generations_menu_items
                if SELECTED_INDEX_GENERATIONS_MENU >= total_generations_menu_items:
                    SELECTED_INDEX_GENERATIONS_MENU = 0
                update_display_generations_menu(SELECTED_INDEX_GENERATIONS_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATIONS_MENU == 0:
                    CURRENT_STATE = GENERATION_I_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 1:
                    CURRENT_STATE = GENERATION_II_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 2:
                    CURRENT_STATE = GENERATION_III_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 3:
                    CURRENT_STATE = GENERATION_IV_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 4:
                    CURRENT_STATE = GENERATION_V_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 5:
                    CURRENT_STATE = GENERATION_VI_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 6:
                    CURRENT_STATE = GENERATION_VII_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 7:
                    CURRENT_STATE = GENERATION_VIII_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATIONS_MENU == 8:
                    CURRENT_STATE = GENERATION_IX_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = MAIN_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_I_MENU_STATE:
        SELECTED_INDEX_GENERATION_I_MENU = 0
        TOTAL_GENERATION_I_MENU_ITEMS = 5
        update_display_generation_i_menu(SELECTED_INDEX_GENERATION_I_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_I_MENU = (
                    SELECTED_INDEX_GENERATION_I_MENU - 1
                ) % TOTAL_GENERATION_I_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_I_MENU < 0:
                    SELECTED_INDEX_GENERATION_I_MENU = TOTAL_GENERATION_I_MENU_ITEMS - 1
                update_display_generation_i_menu(SELECTED_INDEX_GENERATION_I_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_I_MENU = (
                    SELECTED_INDEX_GENERATION_I_MENU + 1
                ) % TOTAL_GENERATION_I_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_I_MENU >= TOTAL_GENERATION_I_MENU_ITEMS:
                    SELECTED_INDEX_GENERATION_I_MENU = 0
                update_display_generation_i_menu(SELECTED_INDEX_GENERATION_I_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_I_MENU == 0:
                    CURRENT_STATE = GENERATION_I_MAIN_REGION_MENU_STATE
                    break
                if SELECTED_INDEX_GENERATION_I_MENU == 1:
                    CURRENT_STATE = GENERATION_I_MOVES_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_II_MENU_STATE:
        SELECTED_INDEX_GENERATION_II_MENU = 0
        TOTAL_GENERATION_II_MENU_ITEMS = 5
        update_display_generation_ii_menu(SELECTED_INDEX_GENERATION_II_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_II_MENU = (
                    SELECTED_INDEX_GENERATION_II_MENU - 1
                ) % TOTAL_GENERATION_II_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_II_MENU < 0:
                    SELECTED_INDEX_GENERATION_II_MENU = (
                        TOTAL_GENERATION_II_MENU_ITEMS - 1
                    )
                update_display_generation_ii_menu(SELECTED_INDEX_GENERATION_II_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_II_MENU = (
                    SELECTED_INDEX_GENERATION_II_MENU + 1
                ) % TOTAL_GENERATION_II_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_II_MENU >= TOTAL_GENERATION_II_MENU_ITEMS:
                    SELECTED_INDEX_GENERATION_II_MENU = 0
                update_display_generation_ii_menu(SELECTED_INDEX_GENERATION_II_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_II_MENU == 0:
                    CURRENT_STATE = GENERATION_II_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_III_MENU_STATE:
        SELECTED_INDEX_GENERATION_III_MENU = 0
        TOTAL_GENERATION_III_MENU_ITEMS = 5
        update_display_generation_iii_menu(SELECTED_INDEX_GENERATION_III_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_III_MENU = (
                    SELECTED_INDEX_GENERATION_III_MENU - 1
                ) % TOTAL_GENERATION_III_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_III_MENU < 0:
                    SELECTED_INDEX_GENERATION_III_MENU = (
                        TOTAL_GENERATION_III_MENU_ITEMS - 1
                    )
                update_display_generation_iii_menu(SELECTED_INDEX_GENERATION_III_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_III_MENU = (
                    SELECTED_INDEX_GENERATION_III_MENU + 1
                ) % TOTAL_GENERATION_III_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_III_MENU
                    >= TOTAL_GENERATION_III_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_III_MENU = 0
                update_display_generation_iii_menu(SELECTED_INDEX_GENERATION_III_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_III_MENU == 0:
                    CURRENT_STATE = GENERATION_III_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_IV_MENU_STATE:
        SELECTED_INDEX_GENERATION_IV_MENU = 0
        TOTAL_GENERATION_IV_MENU_ITEMS = 5
        update_display_generation_iv_menu(SELECTED_INDEX_GENERATION_IV_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_IV_MENU = (
                    SELECTED_INDEX_GENERATION_IV_MENU - 1
                ) % TOTAL_GENERATION_IV_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_IV_MENU < 0:
                    SELECTED_INDEX_GENERATION_IV_MENU = (
                        TOTAL_GENERATION_IV_MENU_ITEMS - 1
                    )
                update_display_generation_iv_menu(SELECTED_INDEX_GENERATION_IV_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_IV_MENU = (
                    SELECTED_INDEX_GENERATION_IV_MENU + 1
                ) % TOTAL_GENERATION_IV_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_IV_MENU >= TOTAL_GENERATION_IV_MENU_ITEMS:
                    SELECTED_INDEX_GENERATION_IV_MENU = 0
                update_display_generation_iv_menu(SELECTED_INDEX_GENERATION_IV_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_IV_MENU == 0:
                    CURRENT_STATE = GENERATION_IV_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_V_MENU_STATE:
        SELECTED_INDEX_GENERATION_V_MENU = 0
        TOTAL_GENERATION_V_MENU_ITEMS = 5
        update_display_generation_v_menu(SELECTED_INDEX_GENERATION_V_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_V_MENU = (
                    SELECTED_INDEX_GENERATION_V_MENU - 1
                ) % TOTAL_GENERATION_V_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_V_MENU < 0:
                    SELECTED_INDEX_GENERATION_V_MENU = TOTAL_GENERATION_V_MENU_ITEMS - 1
                update_display_generation_v_menu(SELECTED_INDEX_GENERATION_V_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_V_MENU = (
                    SELECTED_INDEX_GENERATION_V_MENU + 1
                ) % TOTAL_GENERATION_V_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_V_MENU >= TOTAL_GENERATION_V_MENU_ITEMS:
                    SELECTED_INDEX_GENERATION_V_MENU = 0
                update_display_generation_v_menu(SELECTED_INDEX_GENERATION_V_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_V_MENU == 0:
                    CURRENT_STATE = GENERATION_V_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_VI_MENU_STATE:
        SELECTED_INDEX_GENERATION_VI_MENU = 0
        TOTAL_GENERATION_VI_MENU_ITEMS = 5
        update_display_generation_vi_menu(SELECTED_INDEX_GENERATION_VI_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_VI_MENU = (
                    SELECTED_INDEX_GENERATION_VI_MENU - 1
                ) % TOTAL_GENERATION_VI_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VI_MENU < 0:
                    SELECTED_INDEX_GENERATION_VI_MENU = (
                        TOTAL_GENERATION_VI_MENU_ITEMS - 1
                    )
                update_display_generation_vi_menu(SELECTED_INDEX_GENERATION_VI_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_VI_MENU = (
                    SELECTED_INDEX_GENERATION_VI_MENU + 1
                ) % TOTAL_GENERATION_VI_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VI_MENU >= TOTAL_GENERATION_VI_MENU_ITEMS:
                    SELECTED_INDEX_GENERATION_VI_MENU = 0
                update_display_generation_vi_menu(SELECTED_INDEX_GENERATION_VI_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_VI_MENU == 0:
                    CURRENT_STATE = GENERATION_VI_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_VII_MENU_STATE:
        SELECTED_INDEX_GENERATION_VII_MENU = 0
        TOTAL_GENERATION_VII_MENU_ITEMS = 5
        update_display_generation_vii_menu(SELECTED_INDEX_GENERATION_VII_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_VII_MENU = (
                    SELECTED_INDEX_GENERATION_VII_MENU - 1
                ) % TOTAL_GENERATION_VII_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VII_MENU < 0:
                    SELECTED_INDEX_GENERATION_VII_MENU = (
                        TOTAL_GENERATION_VII_MENU_ITEMS - 1
                    )
                update_display_generation_vii_menu(SELECTED_INDEX_GENERATION_VII_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_VII_MENU = (
                    SELECTED_INDEX_GENERATION_VII_MENU + 1
                ) % TOTAL_GENERATION_VII_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_VII_MENU
                    >= TOTAL_GENERATION_VII_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_VII_MENU = 0
                update_display_generation_vii_menu(SELECTED_INDEX_GENERATION_VII_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_VII_MENU == 0:
                    CURRENT_STATE = GENERATION_VII_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_VIII_MENU_STATE:
        SELECTED_INDEX_GENERATION_VIII_MENU = 0
        TOTAL_GENERATION_VIII_MENU_ITEMS = 5
        update_display_generation_viii_menu(SELECTED_INDEX_GENERATION_VIII_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_VIII_MENU = (
                    SELECTED_INDEX_GENERATION_VIII_MENU - 1
                ) % TOTAL_GENERATION_VIII_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VIII_MENU < 0:
                    SELECTED_INDEX_GENERATION_VIII_MENU = (
                        TOTAL_GENERATION_VIII_MENU_ITEMS - 1
                    )
                update_display_generation_viii_menu(SELECTED_INDEX_GENERATION_VIII_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_VIII_MENU = (
                    SELECTED_INDEX_GENERATION_VIII_MENU + 1
                ) % TOTAL_GENERATION_VIII_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_VIII_MENU
                    >= TOTAL_GENERATION_VIII_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_VIII_MENU = 0
                update_display_generation_viii_menu(SELECTED_INDEX_GENERATION_VIII_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_VIII_MENU == 0:
                    CURRENT_STATE = GENERATION_VIII_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_IX_MENU_STATE:
        SELECTED_INDEX_GENERATION_IX_MENU = 0
        TOTAL_GENERATION_IX_MENU_ITEMS = 5
        update_display_generation_ix_menu(SELECTED_INDEX_GENERATION_IX_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_IX_MENU = (
                    SELECTED_INDEX_GENERATION_IX_MENU - 1
                ) % TOTAL_GENERATION_IX_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_IX_MENU < 0:
                    SELECTED_INDEX_GENERATION_IX_MENU = (
                        TOTAL_GENERATION_IX_MENU_ITEMS - 1
                    )
                update_display_generation_ix_menu(SELECTED_INDEX_GENERATION_IX_MENU)
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_IX_MENU = (
                    SELECTED_INDEX_GENERATION_IX_MENU + 1
                ) % TOTAL_GENERATION_IX_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_IX_MENU >= TOTAL_GENERATION_IX_MENU_ITEMS:
                    SELECTED_INDEX_GENERATION_IX_MENU = 0
                update_display_generation_ix_menu(SELECTED_INDEX_GENERATION_IX_MENU)
            if not button_A.value:
                print("Button A Pressed")
                if SELECTED_INDEX_GENERATION_IX_MENU == 0:
                    CURRENT_STATE = GENERATION_IX_MAIN_REGION_MENU_STATE
                    break
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATIONS_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_I_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU = 0
        generation_i_data = fetch_generation_i_data()
        main_region_data = [generation_i_data["main_region"]]
        TOTAL_GENERATION_I_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_i_main_region_menu(
            SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_I_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_I_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_i_main_region_menu(
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_I_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_I_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU = 0
                update_display_generation_i_main_region_menu(
                    SELECTED_INDEX_GENERATION_I_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_I_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_II_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU = 0
        generation_ii_data = fetch_generation_ii_data()
        main_region_data = [generation_ii_data["main_region"]]
        TOTAL_GENERATION_II_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_ii_main_region_menu(
            SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_II_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_II_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_ii_main_region_menu(
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_II_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_II_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU = 0
                update_display_generation_ii_main_region_menu(
                    SELECTED_INDEX_GENERATION_II_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_II_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_III_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU = 0
        generation_iii_data = fetch_generation_iii_data()
        main_region_data = [generation_iii_data["main_region"]]
        TOTAL_GENERATION_III_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_iii_main_region_menu(
            SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_III_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_III_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_iii_main_region_menu(
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_III_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_III_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU = 0
                update_display_generation_iii_main_region_menu(
                    SELECTED_INDEX_GENERATION_III_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_III_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_IV_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU = 0
        generation_iv_data = fetch_generation_iv_data()
        main_region_data = [generation_iv_data["main_region"]]
        TOTAL_GENERATION_IV_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_iv_main_region_menu(
            SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_IV_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_IV_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_iv_main_region_menu(
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_IV_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_IV_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU = 0
                update_display_generation_iv_main_region_menu(
                    SELECTED_INDEX_GENERATION_IV_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_IV_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_V_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU = 0
        generation_v_data = fetch_generation_v_data()
        main_region_data = [generation_v_data["main_region"]]
        TOTAL_GENERATION_V_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_v_main_region_menu(
            SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_V_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_V_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_v_main_region_menu(
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_V_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_V_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU = 0
                update_display_generation_v_main_region_menu(
                    SELECTED_INDEX_GENERATION_V_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_V_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_VI_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU = 0
        generation_vi_data = fetch_generation_vi_data()
        main_region_data = [generation_vi_data["main_region"]]
        TOTAL_GENERATION_VI_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_vi_main_region_menu(
            SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_VI_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_VI_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_vi_main_region_menu(
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_VI_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_VI_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU = 0
                update_display_generation_vi_main_region_menu(
                    SELECTED_INDEX_GENERATION_VI_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_VI_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_VII_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU = 0
        generation_vii_data = fetch_generation_vii_data()
        main_region_data = [generation_vii_data["main_region"]]
        TOTAL_GENERATION_VII_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_vii_main_region_menu(
            SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_VII_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_VII_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_vii_main_region_menu(
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_VII_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_VII_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU = 0
                update_display_generation_vii_main_region_menu(
                    SELECTED_INDEX_GENERATION_VII_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_VII_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_VIII_MAIN_REGION_MENU_STATE:
        SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU = 0
        generation_viii_data = fetch_generation_viii_data()
        main_region_data = [generation_viii_data["main_region"]]
        TOTAL_GENERATION_VIII_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_viii_main_region_menu(
            SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_VIII_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU < 0:
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_VIII_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_viii_main_region_menu(
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU = (
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_VIII_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_VIII_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU = 0
                update_display_generation_viii_main_region_menu(
                    SELECTED_INDEX_GENERATION_VIII_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_VIII_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_IX_MAIN_REGION_MENU_STATE:
        SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU = 0
        generation_ix_data = fetch_generation_ix_data()
        main_region_data = [generation_ix_data["main_region"]]
        TOTAL_GENERATION_IX_MAIN_REGION_MENU_ITEMS = len(main_region_data)
        update_display_generation_ix_main_region_menu(
            SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU
        )

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU = (
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU - 1
                ) % TOTAL_GENERATION_IX_MAIN_REGION_MENU_ITEMS
                if SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU < 0:
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU = (
                        TOTAL_GENERATION_IX_MAIN_REGION_MENU_ITEMS - 1
                    )
                update_display_generation_ix_main_region_menu(
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU = (
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU + 1
                ) % TOTAL_GENERATION_IX_MAIN_REGION_MENU_ITEMS
                if (
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU
                    >= TOTAL_GENERATION_IX_MAIN_REGION_MENU_ITEMS
                ):
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU = 0
                update_display_generation_ix_main_region_menu(
                    SELECTED_INDEC_GENERATION_IX_MAIN_REGION_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_IX_MENU_STATE
                break

    if CURRENT_STATE == GENERATION_I_MOVES_MENU_STATE:
        SELECTED_INDEX_GENERATION_I_MOVES_MENU = 0
        generation_i_data = fetch_generation_i_data()
        moves_data = generation_i_data.get("moves", [])
        total_generation_i_moves_menu_items = len(moves_data)
        update_display_generation_i_moves_menu(SELECTED_INDEX_GENERATION_I_MOVES_MENU)

        while True:
            if not button_U.value:
                print("Button U Pressed")
                SELECTED_INDEX_GENERATION_I_MOVES_MENU = (
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU - 1
                ) % total_generation_i_moves_menu_items
                if SELECTED_INDEX_GENERATION_I_MOVES_MENU < 0:
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU = (
                        total_generation_i_moves_menu_items - 1
                    )
                update_display_generation_i_moves_menu(
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU
                )
            if not button_D.value:
                print("Button D Pressed")
                SELECTED_INDEX_GENERATION_I_MOVES_MENU = (
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU + 1
                ) % total_generation_i_moves_menu_items
                if (
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU
                    >= total_generation_i_moves_menu_items
                ):
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU = 0
                update_display_generation_i_moves_menu(
                    SELECTED_INDEX_GENERATION_I_MOVES_MENU
                )
            if not button_B.value:
                print("Button B Pressed")
                CURRENT_STATE = GENERATION_I_MENU_STATE
                break
