from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
sq = 1
while(1):
    if(sq == 1):
        while x < 800:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
        sq = 2
        continue
    elif(sq == 2):
        while y < 600:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 2
            delay(0.01)
        sq = 3
        continue
    elif(sq == 3):
        while x > 0:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 2
            delay(0.01)
        sq = 4
        continue
    elif(sq == 4):
        while y > 89:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 2
            delay(0.01)
        sq = 1
        continue

close_canvas()
