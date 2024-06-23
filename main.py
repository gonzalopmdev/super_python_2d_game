import os
from settings import *
import pygame
import sys
from os.path import join
from os.path import dirname, realpath, exists
from level import Level
from pytmx.util_pygame import load_pygame


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Super Pirate World')
        self.clock = pygame.time.Clock()
       
        #Build main route to tmx file
        script_dir = dirname(realpath(__file__))
        self.tmx_path = join(script_dir, 'data', 'levels', 'omni.tmx')

        #Load tmx file
        self.tmx_maps = {0: load_pygame(self.tmx_path)}
        
        self.current_stage = Level(self.tmx_maps[0])
    
        
    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.current_stage.run(dt)        
            pygame.display.update()
            
if __name__ == '__main__':
	game = Game()
	game.run()