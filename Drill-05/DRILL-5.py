from pico2d import *
import os

os.chdir('D:\\공부\\2학년 2학기\\2D 게임프로그래밍\\2017182032-2DGP-DRILL\\Drill-05')

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
pivot = load_image('hand_arrow.png')

running = True
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
prev_x, prev_y = 0, 0
now_x, now_y = 400, 400
goto_x, goto_y = 0, 0
init = 0
frame = 0
clicked = False
hide_cursor()

def handle_events():
    global running
    global x, y
    global goto_x, goto_y
    global prev_x,prev_y
    global init
    global clicked

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            goto_x, goto_y = event.x, KPU_HEIGHT - 1 - event.y
            prev_x, prev_y = now_x, now_y
            clicked = True
            init = 0
    pass


while running:
    if clicked and init < 100 + 1:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        pivot.clip_draw(0, 0, 100, 100, x, y)

        t = init / 100
        now_x = (1 - t) * prev_x + t * goto_x
        now_y = (1 - t) * prev_y + t * goto_y

        character.clip_draw(frame * 100, 0, 100, 100, now_x, now_y)
        update_canvas()
        frame = (frame + 1) % 8
        init +=1
        handle_events()
    else:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        pivot.clip_draw(0, 0, 100, 100, x, y)
        character.clip_draw(frame * 100, 0, 100, 100, now_x, now_y)
        update_canvas()
        frame = (frame + 1) % 8
        handle_events()

close_canvas()