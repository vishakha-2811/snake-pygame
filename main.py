import pygame
import sys
pygame.init()

screen=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
pygame.display.set_caption("🐍 Snake Game 🐍")
snake=pygame.Surface((100,100))
snake.fill((0,200,100))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    screen.blit(snake,(300,300))
    pygame.display.update()
    clock.tick(60)
