from ursina import *
from os import system as run_game
from sys import exit


file_path = __file__
mode = ""
font = "G:/env/main/font.ttf"

def run(option):
    """to display a screen"""
    if option == "3d":
        run_game("python g:/env/main/example/UrsaCraft_video.py")
    elif option == "help":
        run_game("python g:/env/main/main/options.py")

def main_menu():
    """the main menu setup"""

    def start_singleplayer():
        """start game button function"""
        global mode
        mode = "3d"
        run(mode)
        
    def open_options():
        """help menu button function""" 
        global file_path, mode
        mode = "help"
        run(mode)

    def quit_game():
        """exit button function"""
        print(f"\n\n\n\ninfo by the system<main_screen.py>\n\tfile path:{__file__}\n\t<exit form main program>\n\n\n\n")
        exit()

    # Button position
    button_y_start = 0.1
    button_spacing = 0.1

    # Title
    title = Button(text="UrsaCraft",
                 scale=(0.3 * 1.5,0.07 * 1.5),
                 y=button_y_start - (button_spacing * -2.5),
                 z=-0.5,
                 text_color=color.hex("#bd2e3c"),
                 color=color.hex("#FFA8A8"),
                 text_size=4)

    # Start button 
    singleplayer_button = Button(text="Start Game",
                                 scale=(0.3, 0.07),
                                 y=button_y_start,
                                 on_click=start_singleplayer,
                                 color=color.hex("#007fff"),
                                 highlight_scale=1.5)

    # Help button
    options_button = Button(text="Help",
                            scale=(0.3, 0.07),
                            y=button_y_start - (button_spacing * 2),
                            on_click=open_options,
                            color=color.hex("#007fff"),
                            highlight_scale=1.5)

    # Exit button
    quit_button = Button(text="Quit Game",
                         scale=(0.3, 0.07),
                         y=button_y_start - (button_spacing * 3),
                         on_click=quit_game,
                         color=color.red,
                         highlight_scale=1.5)

    # Background
    background_panel = Entity(model='quad', scale_x=camera.aspect_ratio, scale_y=1,
                              texture='assets_main/back_ground.png',
                              parent=camera.ui, z=1) # Render behind UI elements


if __name__ == '__main__':
    print(f"\n\n\n\ninfo by the system<main_screen.py<window>>\nfile path:{__file__}\n\n\n\n")
    app = Ursina()
    print(f"\n\n\n\ninfo by the system<main_screen.py>\n\tfile path:{__file__}\n\n\n\n")
    main_menu()
    def update():
        if held_keys["escape"]:
            print(f"\n\n\n\ninfo by the system<main_screen.py>\n\tfile path:{__file__}\n\t<exit form main program>\n\n\n\n")
            exit()
    app.run()
