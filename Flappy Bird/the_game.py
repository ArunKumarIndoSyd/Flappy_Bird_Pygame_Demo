import pygame,sys,random

def draw_floor():
        screen.blit(floor_surface,(floor_x_pos,800))
        screen.blit(floor_surface,(floor_x_pos+576,800))
def create_pipe():
        random_pipe_position = random.choice(pipe_height)
        print(random_pipe_position)  ##there seems to be a bug over here
        new_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_position))
        return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)


pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
#gravity
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('flappy-bird-assets-master/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('flappy-bird-assets-master/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('flappy-bird-assets-master/sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('flappy-bird-assets-master/sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [200,600,800]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    screen.blit(bg_surface,(0,0))

    #Bird Movement
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)

    #Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)
    #Floor
    floor_x_pos -= 1
    draw_floor()
    floor_x_pos -= 1
    if floor_x_pos <= -576:
        floor_x_pos = 0



    pygame.display.update()
    clock.tick(120)
