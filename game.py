import pygame

import random

#이미지 불러오기
def myimg(img, x,y):
    screen.blit(img, (x,y))



#세팅
t = pygame.init()
pygame.display.set_caption("파이 게임") #<title>

shield = pygame.image.load('resouce\shield.png')

meteor = pygame.image.load('resouce\\운석.png')

speed = 0.5

width = 800
height = 600
r = width*2

x = int(width/2)
y = int(r + 550)

meteor_x = random.randint(0, 800-80)
meteor_y = 0

shield_x = width/2

count = 0

screen  = pygame.display.set_mode((width, height))

finish = False

meteor_speed = 0.2

attack = 0

#데미지 표시
font = pygame.font.Font('freesansbold.ttf', 20) 
text = font.render(f'damageed : {100-attack*4}%', True, (0,0,0), (255,255,255)) 
textRect = text.get_rect()  
textRect.center = (50, 20)
#레벨업 표시
font2 = pygame.font.Font('freesansbold.ttf', 50) 
level = font2.render('LEVEL UP', True, (0, 255, 0), (0, 0,128)) 
levelRect = level.get_rect()  
levelRect.center = (width/2, 40) 

#게임 실생
while not(finish):
    text = font.render(f'damageed : {100-attack*4}%', True, (0,0,0), (255,255,255)) 
    screen.fill((0,0,0))
    screen.blit(text, textRect) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    if event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
        finish = True

    if meteor_speed > 0.6:
        meteor_speed = 0.6

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_a]: shield_x -= speed
    if pressed[pygame.K_d]: shield_x += speed

    if shield_x > 800-95: shield_x -= speed
    if shield_x < 0: shield_x += speed

    # Draw a circle outline
    pygame.draw.circle(screen, (0,162,50), [x,y],r)
 
    myimg(shield, shield_x, 500)
    
    if meteor_y <=  height:
        meteor_y += meteor_speed
    else:
        meteor_y = 0
        meteor_x = random.randint(0,800-80)
        attack += 1
        
        count += 1
    
    if count % 10 == 9 and meteor_speed < 0.6:
        screen.blit(level, levelRect) 

    if count % 10 == 0 and count != 0:
        count += 1
        meteor_speed += 0.05
        speed += 0.02

    
    

    if meteor_x >= shield_x-45 and meteor_x <= shield_x+45 and meteor_y >= 500-100:
        meteor_y = 0
        meteor_x = random.randint(0,800-80)
        
        
        count += 1
        
    if attack == 25:
        finish = True
        
    
        

    screen.blit(meteor, (meteor_x,meteor_y))
    
    pygame.display.flip()
