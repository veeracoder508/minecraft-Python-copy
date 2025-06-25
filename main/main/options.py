from ursina import *
from sys import exit


print(f"\n\n\n\ninfo by the system<options.py<window>>\nfile path:{__file__}\n\n\n\n")
app = Ursina()
print(f"\n\n\n\ninfo by the system<options.py>\n\tfile path:{__file__}\n\n\n\n")
window.title = "help" # Window 
window.always_on_top = True

font = "G:/env/main/font.ttf"


def exit_options():
    """exit the help menu"""
    print(f"\n\n\n\ninfo by the system<options.py>\n\tfile path:{__file__}\n\t<exit form help program>\n\n\n\n")
    exit()

# The button position
button_y_start = 0.1
button_spacing = 0.1

# Title
title = Button(text="HELP MENU",
               scale=(0.3 * 2,0.07 * 2),
               y=button_y_start + (button_spacing * 3),
               color=color.hex("#bd2e3c"),
               text_color=color.hex("#ffa8a8"),
               text_size=4)

# Movement help menu
movement = Button(text="MOVEMENT: WASD",
                             scale=(0.3, 0.07),
                             y=button_y_start,
                             color=color.hex("#007fff"),
                             highlight_scale=1.5)

# Jump help menu
jump = Button(text="JUMP: SPACE",
                            scale=(0.3, 0.07),
                            y=button_y_start - (button_spacing * 2),
                            color=color.hex("#007fff"),
                            highlight_scale=1.5)

# Block selection menu
block = Button(text="1: GRASS 2: DIRT 3: STONE 4: BRICK",
                         scale=((0.3 * 1.5), 0.07),
                         y=button_y_start - (button_spacing * 3),
                         color=color.hex("#007fff"),
                         highlight_scale=1.5)

# Exit button
exit_button = Button(text="EXIT HELP MENU",
                     scale=(0.3,0.07),
                     y=button_y_start - (button_spacing * 4),
                     on_click=exit_options,
                     color = color.red,
                     highlight_scale=1.5)

# Block placement
placement = Button(text="left click: PLACE BLOCK right click: BREAKE BLOCK",
                        scale=((0.3 * 2), 0.07),
                        y=0,
                        color=color.hex("#007fff"),
                        highlight_color=color.hex("#80bfff"),
                        highlight_scale=1.5)

# Background
background_panel = Entity(model='quad', scale_x=camera.aspect_ratio, scale_y=1,
                              texture='assets_main/back_ground.png',
                              parent=camera.ui, z=1) # Render behind UI elements

def update():
        if held_keys["escape"]:
            print(f"\n\n\n\ninfo by the system<main_screen.py>\n\tfile path:{__file__}\n\t<exit form main program>\n\n\n\n")
            exit()


app.run()