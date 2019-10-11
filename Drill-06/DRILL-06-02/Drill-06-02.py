from pico2d import*
import os
import random

os.chdir('D:\\공부\\2학년 2학기\\2D 게임프로그래밍\\2017182032-2DGP-DRILL\\Drill-06\\DRILL-06-02')

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
frame = 0
size = 10
x, y = 100, 100

open_canvas(KPU_WIDTH,KPU_HEIGHT)

character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

random_point = [(random.randint(0,KPU_WIDTH),random.randint(0,KPU_HEIGHT)) for i in range(size)]

def draw_curve_4_points(p1, p2, p3,p4):
    global x,y,frame
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame*100,100,100,100,x,y)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.01)

n = 0
while True:
    draw_curve_4_points(random_point[n],random_point[n+1],random_point[n+2],random_point[n+3])
    n += 1
    if(n >= 7):
        draw_curve_4_points(random_point[7], random_point[8], random_point[9],random_point[0])
        draw_curve_4_points(random_point[8], random_point[9], random_point[0], random_point[1])
        draw_curve_4_points(random_point[9], random_point[0], random_point[1], random_point[2])
        n = 0
