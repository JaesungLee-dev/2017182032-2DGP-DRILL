import game_framework
from pico2d import *
import game_world

# Boy Run Speed
PIXEL_PER_METER = (182.0 / 2.0)  # 182 pixel 2 m
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    def __init__(self):
        self.x, self.y = 800, 300
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 30)
        if self.x >= 1600 - 30 or self.x <= 25:
            self.velocity = -self.velocity
            self.dir = -self.dir
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 182, 336, 182, 168, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * 182, 336, 182, 168,
                                           -3.141592, 'v', self.x, self.y, 182, 168)
