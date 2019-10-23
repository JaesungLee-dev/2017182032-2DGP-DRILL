import game_framework
import main_state
from pico2d import*
import os

#os.chdir('D:\\공부\\2학년 2학기\\2D 게임프로그래밍\\2017182032-2DGP-DRILL\\Drill-08')

pause = None

def enter():
    global pause
    pause = load_image('pause.png')

def exit():
    global pause
    del(pause)

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)

def draw():
    clear_canvas()
    pause.draw(400,300)
    update_canvas()