from config import Config
from graphik import Graphik
from status import Status
import pygame


class OptionsScreen:
    def __init__(self, graphik: Graphik, config: Config, status: Status):
        self.graphik = graphik
        self.config = config
        self.status = status
        self.running = True
    
    def handleKeyDownEvent(self, key):
        if key == pygame.K_ESCAPE:
            return "world"

    def quitApplication(self):
        pygame.quit()
        quit()
    
    def toggleTickSpeedLimit(self):
        if self.config.limitTickSpeed == True:
            self.config.limitTickSpeed = False
        else:
            self.config.limitTickSpeed = True

    def drawLimitTickSpeedButton(self):
        x, y = self.graphik.getGameDisplay().get_size()
        width = x/5
        height = y/10
        xpos = x/2 - width/2
        ypos = y/2 - height/2
        backgroundColor = -1
        if self.config.limitTickSpeed == True:
            backgroundColor = (0,200,0)
        else:
            backgroundColor = (200, 0, 0)
        self.graphik.drawButton(xpos, ypos, width, height, backgroundColor, (0,0,0), 30, "limit TS", self.toggleTickSpeedLimit)

    def drawQuitButton(self):
        x, y = self.graphik.getGameDisplay().get_size()
        width = x/5
        height = y/10
        xpos = x/2 - width/2
        ypos = y/2 - height/2 + width
        self.graphik.drawButton(xpos, ypos, width, height, (255,255,255), (0,0,0), 30, "quit", self.quitApplication)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.KEYDOWN:
                    result = self.handleKeyDownEvent(event.key)
                    if result == "world":
                        return "world"
            
            self.graphik.getGameDisplay().fill((0, 0, 0))
            self.drawLimitTickSpeedButton()
            self.drawQuitButton()
            pygame.display.update()