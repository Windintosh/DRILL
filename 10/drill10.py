from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += 10
        self.frame = (self.frame + 1) % 8
        delay(0.005)

class big_ball:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 599
        self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > 76:
            self.y = self.y - random.randint(1, 20)
        else:
            self.y = 76

class small_ball:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 599
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > 61:
            self.y = self.y - random.randint(1, 20)
        else:
            self.y = 61



def handle_events():
    global runnin1g
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()  #잔디 생성
boy = Boy()
team = [Boy() for i in range(1, 11+1)]
bb = random.randint(1, 20)
sb = 20 - bb
b_balls = [big_ball() for i in range(bb)]
s_balls = [small_ball() for i in range(sb)]

running = True;

# game main loop code
while running:
    handle_events()

    #game logic
    # boy.update()
    for boy in team:
        boy.update()

    for big_ball in b_balls:
        big_ball.update()

    for small_ball in s_balls:
        small_ball.update()

    #game drawing
    clear_canvas()
    grass.draw()
    # boy.draw()
    for boy in team:
        boy.draw()

    for big_ball in b_balls:
        big_ball.draw()

    for small_ball in s_balls:
        small_ball.draw()

    update_canvas()

# finalization code

close_canvas()