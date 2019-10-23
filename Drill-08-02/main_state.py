import random
import json
import os

from pico2d import *

import game_framework

name = "MainState"

boy = None
grass = None
font = None
pause_image = None
pause_mode = False
time = 0

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass, pause_image
    boy = Boy()
    grass = Grass()
    pause_image = load_image('pause.png')


def exit():
    global boy, grass
    del(boy)
    del(grass)

def pause():
    pass


def resume():
    pass


def handle_events():
    global pause_mode

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if pause_mode == False:
                pause_mode = True
            else:
                pause_mode = False
            #game_framework.change_state(pause_state)


def update():
    global time
    if pause_mode == False:
        boy.update()
    else:
        time += 1



def draw():
    global time
    clear_canvas()
    if time > 30:
        pause_image.draw(400,300)
        time = 0
    grass.draw()
    boy.draw()
    update_canvas()




