import pygame
import random
import time
pygame.init()
info = pygame.display.Info()
full_screen_width = info.current_w
full_screen_height = info.current_h

screen = width,height = 600,400

game_window = pygame.display.set_mode(screen,pygame.NOFRAME)
pygame.mixer.music.load('collide.mp3')

fps = 30
clock = pygame.time.Clock()
# Colors
red = (255,0,0)
white = (255,255,255)
yellow = (255,255,0)

# Plank
plank_length,plank_width = 200,10
plank_x,plank_y = random.randint(0,width-plank_length),height-plank_width
move_left = False
move_right = False
level = 1
plank_speed = 10


# Ball
ball_radius = 10
ball_x,ball_y = random.randint(ball_radius,width-ball_radius),random.randint(ball_radius,height-ball_radius-plank_width)
possible_initial_vel = [-5,-4,-3,-2,-1,1,2,3,4,5]
ball_vel_x,ball_vel_y = possible_initial_vel[random.randint(0,9)],possible_initial_vel[random.randint(0,9)]

game_over = False
score = 0
pygame.display.set_caption('Ping Pong Game')
font = pygame.font.SysFont(None, 40)
def print_text(text, color, x, y):
    text = font.render(text, True, color)
    game_window.blit(text, [x, y])


bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,screen)
while not game_over:
    game_window.blit(bg,(0,0))
    # game_window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_RSHIFT:
                plank_speed+=5
            if event.key == pygame.K_LSHIFT:
                plank_speed-=5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            if x< width//2:
                move_left = True
            else:
                move_right = True
        if event.type == pygame.MOUSEBUTTONUP:
            move_left = False
            move_right = False
                
    if move_left:
        if plank_x>=0:
            plank_x-=plank_speed
    if move_right:
        if plank_x < width-plank_length:
            plank_x+=plank_speed
    pygame.draw.rect(game_window,red,(plank_x,plank_y,plank_length,plank_width)) 
    
    ball_x+=ball_vel_x
    ball_y+=ball_vel_y   
    
   
        
        
    pygame.draw.circle(game_window,yellow,(ball_x,ball_y),ball_radius)    
    
    if ball_x-ball_radius<=0 or ball_x+ball_radius>width:
        ball_vel_x = -ball_vel_x
        ball_x+=ball_vel_x
        pygame.mixer.music.play()
    if ball_y-ball_radius<=0:
        ball_vel_y = -ball_vel_y
        ball_y+=ball_vel_y
        pygame.mixer.music.play()

     
                
    if(ball_x >=plank_x and ball_x<=plank_x+plank_length and ball_y+ball_radius >=plank_y and ball_y+ball_radius <= plank_y+plank_width):
        pygame.mixer.music.play()
        ball_vel_y = -ball_vel_y
        score+=5
        fps+=2
        if score%10 == 0:
            if ball_vel_x>0:
                ball_vel_x+=1
            if ball_vel_x<0:
                ball_vel_x-=1
            if ball_vel_y>0:
                ball_vel_y+=1
            if ball_vel_y<0:
                ball_vel_y-=1
        plank_length-=4
    
    print_text(f'Score : {score}',white,0,0)

    if ball_y>height:
        trophy = pygame.image.load('trophy.jpg')
        trophy = pygame.transform.scale(trophy,screen)
        time.sleep(2)
        game_window.blit(trophy,(0,0))
        print_text(f'Your Score : {score}',yellow,width//1.8,height//2)
        print_text('Game Over !',yellow,width//1.8,height//3)
        pygame.display.update()      

        time.sleep(2)
        game_over = True
    pygame.display.update()      
    clock.tick(fps)
    
pygame.quit()
quit()
                