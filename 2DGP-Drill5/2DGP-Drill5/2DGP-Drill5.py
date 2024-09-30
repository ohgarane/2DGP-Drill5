from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
dog = load_image('sprite sheet.png')

def handle_events():
    global running, dir_x, dir_y, state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                state = 'RIGHT'
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                state = 'LEFT'
            elif event.key == SDLK_UP:
                dir_y += 1
                state = 'UP'
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                state = 'DOWN'
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            if dir_x == 0 and dir_y == 0:
                state = 'IDLE'

running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
state = 'IDLE'

while running:
    clear_canvas()
    ground.draw(600, 100)

    if state == 'IDLE':
        dog.clip_composite_draw(0, 768, 256, 256, 0, '', x, y, 128, 128)
    elif state == 'RIGHT':
        dog.clip_composite_draw(frame * 256, 256, 256, 256, 0, '', x, y, 128, 128)
    elif state == 'LEFT':
        dog.clip_composite_draw(frame * 256, 512, 256, 256, 0, '', x, y, 128, 128)
    elif state == 'UP':
        dog.clip_composite_draw(frame * 256, 0, 256, 256, 0, '', x, y, 128, 128)
    elif state == 'DOWN':
        dog.clip_composite_draw(frame * 256, 768, 256, 256, 0, '', x, y, 128, 128)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 4

    x += dir_x * 10
    y += dir_y * 10

    x = clamp(25, x, 800 - 25)
    y = clamp(50, y, 600 - 50)

    delay(0.05)

close_canvas()
