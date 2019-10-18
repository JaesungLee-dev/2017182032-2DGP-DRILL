from pico2d import *
import random
import os

os.chdir('D:\\공부\\2학년 2학기\\2D 게임프로그래밍\\2017182032-2DGP-DRILL\\Drill-07')

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0,700), 600
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(1,10)

    def update(self):
        if self.y > 60:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
team = [Boy() for i in range(11)]
grass = Grass()
balls = [Ball() for n in range(20)]
running = True

while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)

close_canvas()
