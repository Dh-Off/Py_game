#배경이미지 
import pygame, os

pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("Spider_man")     #게임제목
clock = pygame.time.Clock()

#배경 불러오기
current_path = os.path.dirname(__file__)  #현재 파일 위치반환
back = pygame.image.load(os.path.join(current_path, "back.png"))


running = True
while running:
    clock.tick(30)  #FPS 30고정  게임속도 일정.
    for event in pygame.event.get():       #이벤트 반복 확인. 이벤트 받아오기
        if event.type == pygame.QUIT:
            running = False
    screen.blit(back, (0,0) ) #배경, 위치(x,y)
    pygame.display.update()

pygame.quit() #진짜종료