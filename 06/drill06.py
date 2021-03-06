from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
sq = 1
sin = 0
cos = 180
xmov = 0
ymov = 0
xbuf = 0
ybuf = 0
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
        sq = 5
        continue
    elif(sq == 5):
        while x < 400:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
        sq = 6
        continue
    elif(sq == 6):
        xbuf = x
        ybuf = y
        while sin < 360:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            xmov = 200 * math.sin(sin / 360 * 2 * math.pi)
            ymov = 200 * math.cos(cos / 360 * 2 * math.pi)
            x = xbuf + xmov
            y = ybuf + ymov + 200
            sin += 2
            cos += 2
            delay(0.01)
        sq = 1
        sin = 0
        cos = 180
        continue
close_canvas()
