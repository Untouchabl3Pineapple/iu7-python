import sys, pygame

# ___________________________InitPyGame_____________________________
 
pygame.init()
 
size = width, height = 1250, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animation by Artemev Ilya IU7-23B")
clock = pygame.time.Clock()

# ___________________________ImportImages_____________________________

ball = pygame.image.load("ball.png")
bg_game = pygame.image.load("bg_game.jpg")
bg_exit = pygame.image.load("bg_exit.jpg")
car = pygame.image.load("car_left1.png")
 
walk_left = [pygame.image.load("car_left1.png"), pygame.image.load("car_left2.png")]
walk_right = [pygame.image.load("car_right1.png"), pygame.image.load("car_right2.png")]
 
# ___________________________GlobalVars_____________________________

FPS = 100
counter_pos = 0
x_car = width // 2
y_car = height // 2 + 80
x_ball = 100
y_ball = 100
min_x = -4
max_x = width - 285
flag = False
left = False
right = False

# ___________________________StartPositions_________________________

screen.blit(bg_game, (0, 0))
screen.blit(ball, (x_ball, y_ball))
screen.blit(walk_right[0], (x_car, y_car))
pygame.display.update()
    
# ___________________________EventProcess___________________________

run = True
while run:

    clock.tick(FPS)
    
    # ___________________________Exit________________________________
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    if counter_pos + 1 >= 15:
        counter_pos = 0
        
    # ___________________________Ball+Miss__________________________________________________
        
    if y_ball != 550:
        if right == True and x_car - 70 < x_ball < x_car + 70 and y_ball == y_car: flag = True
        if left == True and x_car + 100 < x_ball < x_car + 200 and y_ball == y_car: flag = True
        if flag == False:
            x_ball += 1
            y_ball += 2
        else:
            if left == True:
                x_ball = x_car + 205
                y_ball = y_car + 7
            else:
                x_ball = x_car + 35
                y_ball = y_car + 7
            
        screen.blit(ball, (x_ball, y_ball))
    else:
        screen.blit(bg_exit, (0, 0))
        pygame.display.update()
        pygame.time.wait(1000)
        exit()
        
    # ___________________________Car________________________________
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x_car <= min_x: x_car = min_x
        x_car -= 7
        screen.blit(walk_left[counter_pos // 8], (x_car, y_car))
        counter_pos += 1
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        if x_car >= max_x: x_car = max_x
        x_car += 7
        screen.blit(walk_right[counter_pos // 8], (x_car, y_car))
        counter_pos += 1
        left = False
        right = True
    else:
        if left == True: screen.blit(walk_left[counter_pos // 8], (x_car, y_car))
        else: screen.blit(walk_right[counter_pos // 8], (x_car, y_car))
        
    
    pygame.display.update()

    
    screen.blit(bg_game, (0, 0))
    
# _____________________________________________________________
