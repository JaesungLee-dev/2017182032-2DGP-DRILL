import random
from pico2d import *
import game_world
import game_framework

#1280, 1024

BIG, SMALL = range(2)

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(20, 1800 - 20), random.randint(20, 1100 - 20)

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.size = SMALL

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom

        self.image.draw(cx,cy)

    def update(self):
        pass

    def set_background(self, bg):
        self.bg = bg

    def stop(self):
        pass


class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(20, 1280 - 20), random.randint(20, 1024 - 20)
        self.size = BIG

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20