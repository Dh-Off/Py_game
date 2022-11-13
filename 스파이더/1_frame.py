#뼈대

import pygame

pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("Spider_man")     #게임제목
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(30)  #FPS 30고정  게임속도 일정.
    for event in pygame.event.get():       #이벤트 반복 확인. 이벤트 받아오기
        if event.type == pygame.QUIT:
            running = False
    

pygame.quit() #진짜종료