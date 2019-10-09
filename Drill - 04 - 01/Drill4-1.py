from pico2d import *
import os

os.chdir('D:\\공부\\2학년 2학기\\2D 게임프로그래밍\\2017182032-2DGP-DRILL\\Drill - 04 - 01')

open_canvas()
grass = load_image('grass.png')
character_animation = load_image('animation_sheet.png')
dir = 0
running = True
animation_y = 0
frame = 0
x = 400


def handle_events():
    global running
    global dir
    global animation_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                animation_y = 100
            elif event.key == SDLK_LEFT:
                dir -= 1
                animation_y = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
    pass

while running:
    clear_canvas()
    grass.draw(400,30)
    character_animation.clip_draw(frame * 100,animation_y,100,100,x,90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x > 10 and x < 800:
        x += dir * 5
    elif x <= 10:
        x += 5
    elif x >=800:
        x -= 5

    #delay(0.01)

close_canvas()
