from random import randint

import pygame
from dino_runner.components.obstacles.shield import Shield
from dino_runner.components.obstacles.hammer import Hammer
import random

class PowerUpManager ():
    def __init__ (self):
        self.power_ups = []
        self.when_appears = randint(200, 300)
        self.power_up_k = 0
    
    def generate_power_up (self):
        if len (self.power_ups) == 0 and self.when_appears == self.power_up_k:
            self.choose = random.randint(0, 1)
            if self.choose == 0:
                self.power_ups.append(Shield())
            elif self.choose == 1:
                 self.power_ups.append(Hammer())

    def update (self, game_speed, player):
        self.power_up_k += 1
        if self.power_up_k > 400:
            self.power_up_k = 0
        self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up.start_time, power_up.duration, power_up.type)
                self.power_ups.remove(power_up)

    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset_power_ups(self):
        self.power_ups = []