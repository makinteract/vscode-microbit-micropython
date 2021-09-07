class _Image:
    """Base image class"""

    def width(self):
        """gets the number of columns in an image"""
        return 5

    def height(self):
        """gets the number of rows in an image"""
        return 5

    def set_pixel(self,x,y,value):
        """sets the brightness of a pixel at the given position
        Cannot be used on inbuilt images."""
        a = 0

    def get_pixel(self,x,y):
        """returns the brightness of the pixel located at x,y"""
        return 9

    def shift_left(self,n):
        """returns a new image created by shifting the image left by n columns"""
        return _Image()

    def shift_right(self,n):
        """returns a new image created by shifting the image right by n columns"""
        return _Image()

    def shift_up(self,n):
        """returns a new image created by shifting the image up by n rows"""
        return _Image()

    def shift_down(self,n):
        """returns a new image created by shifting the image down by n rows"""
        return _Image()

    def crop(self,x,y,w,h):
        """return a new image by cropping the picture to a width of w and a height of h, starting with the pixel at column x and row y."""
        return _Image()

    def copy(self):
        """return an exact copy of the image"""
        return _Image()

    def invert(self):
        """return a new image by inverting the brightness of the pixels in the source image."""
        return _Image()

    def fill(self,value):
        """Return a new image by inverting the brightness of the pixels in the source image.
        Cannot be used on inbuilt images."""
        return _Image()

    def blit(self,src, x, y, w, h, xdest=0, ydest=0):
        """Copy the rectangle defined by x, y, w, h from the image src into this image at xdest, ydest. Areas in the source rectangle, but outside the source image are treated as having a value of 0."""
        a = 0

HEART = _Image
HEART_SMALL = _Image

HAPPY = _Image
SMILE = _Image
SAD = _Image
CONFUSED = _Image
ANGRY = _Image
ASLEEP = _Image
SURPRISED = _Image
SILLY = _Image
FABULOUS = _Image
MEH = _Image

YES = _Image
NO = _Image

CLOCK12 = _Image
CLOCK11 = _Image
CLOCK10 = _Image
CLOCK9 = _Image
CLOCK8 = _Image
CLOCK7 = _Image
CLOCK6 = _Image
CLOCK5 = _Image
CLOCK4 = _Image
CLOCK3 = _Image
CLOCK2 = _Image
CLOCK1 = _Image

ARROW_N = _Image
ARROW_NE = _Image
ARROW_E = _Image
ARROW_SE = _Image
ARROW_S = _Image
ARROW_SW = _Image
ARROW_W = _Image
ARROW_NW = _Image

TRIANGLE = _Image
TRIANGLE_LEFT = _Image
CHESSBOARD = _Image
DIAMOND = _Image
DIAMOND_SMALL = _Image
SQUARE = _Image
SQUARE_SMALL = _Image

RABBIT = _Image
COW = _Image

MUSIC_CROTCHET = _Image
MUSIC_QUAVER = _Image
MUSIC_QUAVERS = _Image

PITCHFORK = _Image

XMAS = _Image

PACMAN = _Image
TARGET = _Image
TSHIRT = _Image
ROLLERSKATE = _Image
DUCK = _Image
HOUSE = _Image
TORTOISE = _Image
BUTTERFLY = _Image
STICKFIGURE = _Image
GHOST = _Image
SWORD = _Image
GIRAFFE = _Image
SKULL = _Image
UMBRELLA = _Image
SNAKE = _Image