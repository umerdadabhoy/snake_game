from typing import Counter
import pygame
import random
from pygame.rect import Rect
from win32api import GetSystemMetrics
pygame.init()

#get pc window
window = GetSystemMetrics
width_w = window(0)
height_w = window(1)
screen = pygame.display.set_mode((width_w/1.25,height_w/1.25)) 
screen_rect = Rect(0,0, width_w/1.25, height_w/1.25)
background_color = 'limegreen'
game_name = "SNAKER's"
screen.fill(background_color)
pygame.display.set_caption(game_name)

random_point = random.randint(2,50)

x_snake = int(width_w/random_point) 
y_snake = int(height_w/random_point)

score = 0
length_of_snake =  1
x_food , y_food = 0,0
toss = random.randint(1,2)
lastkey= None
timer = 0

font = pygame.font.SysFont('Arial',14)

snake = font.render("#",True,'yellow')
snake_head = font.render("O",True,'black')
snake_size = 14

food = font.render('$',True,'red')




def draw_snake(x,y,scr,sz):
    snake_line = []
    

    for i in range(score+1):
    
        if lastkey == pygame.K_UP:
            y=y+10 
        elif lastkey ==pygame.K_DOWN:
             y=y-10
        elif lastkey == pygame.K_RIGHT:
            x=x-10 
        elif lastkey ==pygame.K_LEFT:   
            x=x+10
        
        snake_rect = pygame.Rect(x,y,sz,sz)
        if not screen_rect.contains(snake_rect):
            x = snake_rect.left
            y = snake_rect.top
            snake_rect.clamp_ip(screen_rect)

        snake = pygame.draw.rect(scr,background_color,snake_rect)

        snake_line.append(snake)

    return snake_line



def light_up(skin,shape):
        screen.blit(skin, skin.get_rect(center = shape.center))


def random_food(point):
    food_coordinate = random.randint(0,window(point)/1.25)
    return food_coordinate


while True: 
# for loop through the event queue  
    for event in pygame.event.get():   
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            exit(1)    
        #check for event
        if event.type == pygame.KEYDOWN:
            lastkey = event.key

    #necessary to fill again to avoid continoous rectangles
    screen.fill(background_color)
    #drawing snake , first part
    rectangle_snake = draw_snake(x_snake,y_snake,screen,snake_size)
    rectangle_food = pygame.draw.rect(screen,background_color,pygame.Rect(x_food,y_food,14,14))
    
    for i in range(len(rectangle_snake)):
        if i == 0 :
            light_up(snake_head,rectangle_snake[i])
        else:
            light_up(snake,rectangle_snake[i])

        if (x_food-10 <= x_snake <= x_food+10 )and (y_food-10 <= y_snake <= y_food+10):
            x_food = random_food(0)
            y_food = random_food(1)
            score = score + 1
        else:
            light_up(food,rectangle_food)
    
    score_text = font.render(str(score),True,'pink') 
    screen.blit(score_text, ((width_w-10)/1.25,10))     
    pygame.display.update()
    
    val = 0.1
    if lastkey == None:
        if toss == 1:
            x_snake += val
        else:
            y_snake += val
    elif lastkey == pygame.K_UP:

        y_snake-=val
        
    elif lastkey == pygame.K_DOWN:

        y_snake+=val

    elif lastkey == pygame.K_RIGHT:

        x_snake+=val

    elif lastkey == pygame.K_LEFT:

        x_snake-=val

 