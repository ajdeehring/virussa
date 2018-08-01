import pygame
from pygame.locals import*
import random
from virus import VirusNode
pygame.init()

size = (width, height) = (850, 480)
color = (150, 0, 42)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

num_docs = 1
num_bac = 5
split_time = 500
done = False
bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()
def process_events():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
def main():
    #in your imports: from virus import VirusNode
    bacteria.add(VirusNode((random.randint(50, width - 50),
                            random.randint(50, height - 50)), split_time))
    while not done:
        clock.tick(60)
        process_events()
        bacteria.update()
        screen.fill(color)
        doctors.draw(screen)
        bacteria.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()