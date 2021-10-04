from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image("hand_arrow.png")

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
chx, chy = KPU_WIDTH // 2, KPU_HEIGHT // 2
dir = 1
frame = 0
hide_cursor()
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if dir == 1:
        if x == chx and y == chy:
            character.clip_draw(100, 100 * 1, 100, 100, chx, chy)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, chx, chy)

    elif dir == -1:
        if x == chx and y == chy:
            character.clip_composite_draw(100, 100 * 1, 100, 100, 0, 'h', chx, chy, 100, 100)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h',  chx, chy, 100, 100)
    cursor.draw(x, y, 50, 50)
    if x > chx and y>chy:
        chx = chx + 1
        chy = chy + 1
        dir = 1
    elif x < chx and y<chy:
        chx = chx - 1
        chy = chy - 1
        dir = -1
    elif x > chx and y < chy:
        chx += 1
        chy -= 1
        dir = 1
    elif x < chx and y > chy:
        chx -= 1
        chy += 1
        dir = -1
    elif x > chx and y == chy:
        chx += 1
        dir = 1
    elif x < chx and y == chy:
        chx -= 1
        dir = -1
    if y > chy and x == chx:
        chy += 1
    elif y < chy and x == chx:
        chy -= 1
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()

