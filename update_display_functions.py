""" Sets up each individual display """

from display import (
    disp,
    clear_buffer,
    buffer_main_menu,
    draw_main_menu,
    buffer_generations_menu,
    draw_generations_menu,
    buffer_generation_i_menu,
    draw_generation_i_menu,
    buffer_generation_ii_menu,
    draw_generation_ii_menu,
    buffer_generation_iii_menu,
    draw_generation_iii_menu,
    buffer_generation_iv_menu,
    draw_generation_iv_menu,
    buffer_generation_v_menu,
    draw_generation_v_menu,
    buffer_generation_vi_menu,
    draw_generation_vi_menu,
    buffer_generation_vii_menu,
    draw_generation_vii_menu,
    buffer_generation_viii_menu,
    draw_generation_viii_menu,
    buffer_generation_ix_menu,
    draw_generation_ix_menu,
    buffer_generation_i_main_region_menu,
    draw_generation_i_main_region_menu,
    buffer_generation_ii_main_region_menu,
    draw_generation_ii_main_region_menu,
    buffer_generation_iii_main_region_menu,
    draw_generation_iii_main_region_menu,
    buffer_generation_iv_main_region_menu,
    draw_generation_iv_main_region_menu,
    buffer_generation_v_main_region_menu,
    draw_generation_v_main_region_menu,
    buffer_generation_vi_main_region_menu,
    draw_generation_vi_main_region_menu,
    buffer_generation_vii_main_region_menu,
    draw_generation_vii_main_region_menu,
    buffer_generation_viii_main_region_menu,
    draw_generation_viii_main_region_menu,
    buffer_generation_ix_main_region_menu,
    draw_generation_ix_main_region_menu,
    buffer_generation_i_moves_menu,
    draw_generation_i_moves_menu,
)


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
