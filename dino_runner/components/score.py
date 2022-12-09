

import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0

    def update (self, game):
        self.score +=1
        if self.score % 100 == 0:
            game.game_speed += 2
        elif self.score > self.high_score:
            self.high_score = self.score

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_component = font.render(f"Score:{self.score}     Highscore:{self.high_score}", True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (800, 50)
        screen.blit(text_component,text_rect)

    def reset(self):
        self.score=0