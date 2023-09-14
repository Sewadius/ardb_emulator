import pyglet
from arduboy import Arduboy

# Arduboy constructor. (x size, y size, scale)
arduboy = Arduboy(128, 64, 5)
# Create window to display Arduboy emulation
window = pyglet.window.Window(arduboy.width*arduboy.scale, arduboy.height*arduboy.scale, "Arduboy Emulator")


@window.event
def on_draw():
    window.clear()
    run_code()


def run_code():
    arduboy.clear_display()
    arduboy.draw_pixel(5, 15)
    arduboy.draw_char(0, 20, 'A', 1)
    arduboy.display()


pyglet.app.run()
