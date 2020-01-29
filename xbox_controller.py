import sys
import pygame
pygame.init()

from threading import Thread

class XboxController(Thread):
    def __init__(self):
        """
        """
        super(XboxController, self).__init__()
        self.keepPlaying = True
        self.joysticks = []
        self.clock = pygame.time.Clock()
        self.button = None
        self.hat = None
        self.current_cmd = ''
        self.key_map = {0:'A', 1:'B', 2:'X', 3:'Y', 4:'LB', 5:'RB', 6:'LB', 7:'RB', 8:'POWER', (0, 1):'UP', (0, -1):'DOWN', (-1, 0):'LEFT', (1, 0):'RIGHT'}

    def initialize_joysticks(self):
        # for al the connected joysticks
        for i in range(0, pygame.joystick.get_count()):
            # create an Joystick object in our list
            self.joysticks.append(pygame.joystick.Joystick(i))
            # initialize them all (-1 means loop forever)
            self.joysticks[-1].init()
            # print a statement telling what the name of the controller is
            print ("Detected joystick "),self.joysticks[-1].get_name(),"'"

    def run_control(self):
        while self.keepPlaying:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    self.button = event.__dict__['button']
                    self.current_cmd = self.key_map[self.button]
                elif event.type == pygame.JOYBUTTONUP:
                    self.current_cmd = ''
                elif event.type == pygame.JOYHATMOTION:
                    self.hat = event.__dict__['value']
                    if self.hat not in [(0, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                        self.current_cmd = self.key_map[self.hat]
                    else:
                        self.current_cmd = ''
