import pygame
from pygame.locals import *
import random
from virus import VirusNode
from doctor import Doctor

pygame.init()

size = (width, height) = (850, 480)
color = (255, 255, 255)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 70)
num_docs = 1
num_bac = 5
done = False
bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()
split_time = 500


def process_events():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

def init():
    for i in range(num_bac):
        bacteria.add(VirusNode((random.randint(50, width - 50),
                                random.randint(50, height - 50)), split_time))
    for i in range(num_docs):
        doctors.add(Doctor((random.randint(50, width - 50),
                            random.randint(50, height - 50))))


split_times = 10
def main():
    init()
    while not done:
        clock.tick(60)
        process_events()
        if len(bacteria) > num_bac*split_times:
            text = font.render("You have been overrun",True,(255,0,0))
            text_rect = text.get_rect()
        elif len(bacteria) == 0:
            text = font.render("Outbreak stopped", True, (255, 0, 0))
            text_rect = text.get_rect()
        else:
            bacteria.update()
            doctors.update()
            pygame.sprite.groupcollide(doctors,bacteria,False,True)
            text = font.render("Bacteria Count: {}".format(len(bacteria)),
                               True, (255, 0, 0))
            text_rect = text.get_rect()

        screen.fill(color)
        bacteria.draw(screen)
        doctors.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
