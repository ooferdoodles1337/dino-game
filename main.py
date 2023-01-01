import pygame as pg
import os

pg.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pg.image.load(os.path.join('Assets', 'Dino', 'DinoRun1.png')),
           pg.image.load(os.path.join('Assets', 'Dino', 'DinoRun2.png'))]

JUMPING = pg.image.load(os.path.join('Assets', 'Dino', 'DinoJump.png'))

DUCKING = [pg.image.load(os.path.join('Assets', 'Dino', 'DinoDuck1.png')),
           pg.image.load(os.path.join('Assets', 'Dino', 'DinoDuck2.png'))]

SMALL_CACTUS = [pg.image.load(os.path.join('Assets', 'Cactus', 'SmallCactus1.png')),
                pg.image.load(os.path.join('Assets', 'Cactus', 'SmallCactus2.png')),
                pg.image.load(os.path.join('Assets', 'Cactus', 'SmallCactus3.png'))]

LARGE_CACTUS = [pg.image.load(os.path.join('Assets', 'Cactus', 'LargeCactus1.png')),
                pg.image.load(os.path.join(
                    'Assets', 'Cactus', 'LargeCactus2.png')),
                pg.image.load(os.path.join('Assets', 'Cactus', 'LargeCactus3.png'))]

BIRD = [pg.image.load(os.path.join('Assets', 'Bird', 'Bird1.png')),
        pg.image.load(os.path.join('Assets', 'Bird', 'Bird2.png'))]

CLOUD = pg.image.load(os.path.join('Assets', 'Other', 'Cloud.png'))

BG = pg.image.load(os.path.join('Assets', 'Other', 'Track.png'))


class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pg.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pg.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pg.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        pass

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


def main():
    run = True
    clock = pg.time.Clock()
    player = Dinosaur()

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        userInput = pg.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pg.display.update()


main()