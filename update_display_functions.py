""" Contains all update display functions """



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
