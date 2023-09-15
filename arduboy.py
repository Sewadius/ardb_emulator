import pyglet


class Arduboy:
    cursor_x, cursor_y = 0, 0
    text_size = 1
    height, width, scale = [None] * 3
    sBuffer = []

    def __init__(self, x, y, s):
        self.width, self.height = x, y
        self.scale = s

    # void blank();
    def blank(self):
        self.clear_display()
        self.draw_screen()

    # void clearDisplay();
    def clear_display(self):
        for _ in range(self.width):
            for _ in range(self.height):
                self.sBuffer.append(0)

    # void display();
    def display(self):
        self.draw_screen(self.sBuffer)

    # void drawBitmap(int16_t x, int16_t y, const uint8_t *bitmap, int16_t w, int16_t h, uint8_t color);
    def draw_bitmap(self):
        # todo: implement drawBitmap
        pass

    # void drawChar(int16_t x, int16_t y, unsigned char c, uint8_t color, uint8_t bg, uint8_t size);
    # Font Minecraftia: http://www.dafont.com/es/minecraftia.font
    def draw_char(self, x, y, c, size):
        if len(c) == 1:
            label = pyglet.text.Label(c,
                                      font_name='Minecraftia',
                                      font_size=size * self.scale * 6,
                                      x=x * self.scale, y=(63 - y) * self.scale)
            label.draw()

    # void drawPixel(int x, int y, uint8_t color);
    def draw_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.sBuffer[x * self.height + y] = 1

    # void drawScreen(const unsigned char *image);
    # void drawScreen(unsigned char image[]);
    def draw_screen(self, image):
        for x in range(self.width):
            for y in range(self.height):
                if image[x * self.height + y] == 1:
                    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS)

    # ('v2i', [x * self.scale,
    #       (63 - y) * self.scale,
    #                                                                          x * self.scale + self.scale,
    #                                                                          (63 - y) * self.scale,
    #                                                                          x * self.scale + self.scale,
    #                                                                          (63 - y) * self.scale + self.scale,
    #                                                                          x * self.scale,
    #                                                                          (63 - y) * self.scale + self.scale])


    # void setCursor(int16_t x, int16_t y);

    def set_cursor(self, x, y):
        self.cursor_x, self.cursor_y = x, y

    # void setTextSize(uint8_t s);
    def set_text_size(self, size):
        self.text_size = size * self.scale * 6

    # TODO: original functions to be implemented
    # Test
    # void start();
    # void idle();
    #
    # void clearDisplay();
    # void display();
    # void drawScreen(const unsigned char *image);
    # void drawScreen(unsigned char image[]);
    # void drawPixel(int x, int y, uint8_t color);
    # uint8_t getPixel(uint8_t x, uint8_t y);
    # void drawCircle(int16_t x0, int16_t y0, int16_t r, uint8_t color);
    # void drawCircleHelper(int16_t x0, int16_t y0, int16_t r, uint8_t cornername, uint8_t color);
    # void fillCircle(int16_t x0, int16_t y0, int16_t r, uint8_t color);
    # void fillCircleHelper(int16_t x0, int16_t y0, int16_t r, uint8_t cornername, int16_t delta, uint8_t color);
    # void drawLine(int16_t x0, int16_t y0, int16_t x1, int16_t y1, uint8_t color);
    # void drawRect(int16_t x, int16_t y, int16_t w, int16_t h, uint8_t color);
    # void drawFastVLine(int16_t x, int16_t y, int16_t h, uint8_t color);
    # void drawFastHLine(int16_t x, int16_t y, int16_t w, uint8_t color);
    # void fillRect(int16_t x, int16_t y, int16_t w, int16_t h, uint8_t color);
    # void fillScreen(uint8_t color);
    # void drawRoundRect(int16_t x, int16_t y, int16_t w, int16_t h, int16_t r, uint8_t color);
    # void fillRoundRect(int16_t x, int16_t y, int16_t w, int16_t h, int16_t r, uint8_t color);
    # void drawTriangle(int16_t x0, int16_t y0, int16_t x1, int16_t y1, int16_t x2, int16_t y2, uint8_t color);
    # void fillTriangle (int16_t x0, int16_t y0, int16_t x1, int16_t y1, int16_t x2, int16_t y2, uint8_t color);
    # void drawBitmap(int16_t x, int16_t y, const uint8_t *bitmap, int16_t w, int16_t h, uint8_t color);
    # void drawSlowXYBitmap(int16_t x, int16_t y, const uint8_t *bitmap, int16_t w, int16_t h, uint8_t color);
    # void drawChar(int16_t x, int16_t y, unsigned char c, uint8_t color, uint8_t bg, uint8_t size);
    #
    #
    # void setTextWrap(boolean w);
    # inline unsigned char* getBuffer();
    # uint8_t width();
    # uint8_t height();
    # virtual size_t write(uint8_t);
    # void swap(int16_t& a, int16_t& b);
