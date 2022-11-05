""" cave - Copyright 2016 Kenichiro Tanaka  """
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()  #초기화
pygame.key.set_repeat(5, 5)  #키 반복설정(지연시간:msc, 간격:msec)
SURFACE = pygame.display.set_mode((800, 600))       #게임 화면크기
FPSCLOCK = pygame.time.Clock()

def main():
    """ 메인 루틴 """
    walls = 80
    ship_y = 250  #캐릭터 y좌표
    velocity = 0  #상하이동
    score = 0
    slope = randint(1, 6)  #동굴 기울
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400)) #겜 시작시 동굴의 직사각형
    game_over = False

    while True:   #게임 루틴추가
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        # 내 캐릭터를 이동
        if not game_over:
            score += 10                 #▽velocity -값이 줄이면 천천히 올라감
            velocity += -3 if is_space_down else 3   
            ship_y += velocity   

            # 동굴을 스크롤
            edge = holes[-1].copy()  #동굴 마지막블록 제일 오른쪽꺼 복사
            test = edge.move(0, slope)  #움직인 조각은 test로 저장 #기울기만큼 이동한 조각을 test
            if test.top <= 0 or test.bottom >= 600:  #위나 아래에 닿으면 slope다시조절
                slope = randint(1, 6) * (-1 if slope > 0 else 1) #양수였으면 음수, 음수였으면 양수
                edge.inflate_ip(0, -20) #새로운slope설정되면 #inflate_ip "자신"이 늘거나 주는거 동굴크기 20만큼 줄어듬
            edge.move_ip(10, slope) #마지막 조각을 움직여서 붙임
            holes.append(edge)
            del holes[0]
            holes = [x.move(-10, 0) for x in holes] #전체 조각을 앞으로 당김

            # 충돌?       #Y좌표가 동굴 위를 뚫거나 바닥밑으로가면
            if holes[0].top > ship_y or \
                holes[0].bottom < ship_y + 80:
                game_over = True

        # 그리기
        if score == 1000:
            SURFACE.fill((0, 255, 255))
        SURFACE.fill((0, 255, 0))
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y-40))

        pygame.display.update()
        FPSCLOCK.tick(15)  #1초당 15회 반복 (프레임, 클수록 빨라짐)

if __name__ == '__main__':
    main()
