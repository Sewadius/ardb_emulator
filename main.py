import pyglet
from arduboy import Arduboy

# Arduboy constructor. (x size, y size, scale)
ad = Arduboy(128, 64, 5)
# Create window to display Arduboy emulation
window = pyglet.window.Window(ad.width * ad.scale, ad.height * ad.scale, "Arduboy Emulator")


@window.event
def on_draw():
    window.clear()
    run_code()


def run_code():
    ad.clear_display()
    ad.draw_pixel(5, 15)
    ad.draw_char(0, 20, 'A', 1)
    ad.draw_char(10, 20, 'B', 1)
    ad.draw_char(20, 20, 'C', 1)
    # ad.display()


if __name__ == '__main__':
    pyglet.app.run()
