""" Contains all update display functions """

from buffer_and_drawing_objects import (
    clear_buffer,
    disp,
    buffer_generations_menu,
    draw_generations_menu,
    buffer_main_menu,
    draw_main_menu,
    buffer_generation_i_menu,
    draw_generation_i_menu,
    buffer_generation_ii_menu,
    draw_generation_ii_menu,
)

from fetch_api_data import fetch_generation_data

def update_display_generations_menu(selected_index):
    """Creates generations menu display"""
    clear_buffer(buffer_generations_menu, draw_generations_menu)
    draw_generations_menu.text((0, 0), "Generations:", fill=1)

    generation_results, total_generations_menu_items = fetch_generation_data()

    display_count = 5
    start_index_generations_menu = 0
    max_visible_items = min(
        display_count, total_generations_menu_items - start_index_generations_menu
    )


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

def update_display_main_menu(selected_index):
    """Creates main display menu"""
    clear_buffer(buffer_main_menu, draw_main_menu)
    draw_main_menu.text((0, 0), "PokeDictionary", fill=1)

    main_menu_items = ["Generations", "Items", "Pokemon"]

    for i, item in enumerate(main_menu_items):
        display_text = item

        if i == selected_index:
            display_text = f"# {display_text}"

        draw_main_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_main_menu)
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

        if i == selected_index:
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

        if i == selected_index:
            display_text = f"# {display_text}"

        draw_generation_ii_menu.text((0, (i * 10) + 10), display_text, fill=1)

    disp.image(buffer_generation_ii_menu)
    disp.show()
