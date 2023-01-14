from time import sleep
from config.config import Config
from lib.graphik.src.graphik import Graphik
from screen.screens import ScreenString
from ui.status import Status
import pygame

# @author Daniel McCoy Stephenson
class ConfigScreen:
    def __init__(self, graphik: Graphik, config: Config, status: Status):
        self.graphik = graphik
        self.config = config
        self.status = status
        self.running = True
        self.nextScreen = ScreenString.MAIN_MENU_SCREEN
        self.changeScreen = False
    
    def handleKeyDownEvent(self, key):
        if key == pygame.K_ESCAPE:
            self.switchToMainMenuScreen()
    
    def switchToMainMenuScreen(self):
        self.nextScreen = ScreenString.MAIN_MENU_SCREEN
        self.changeScreen = True

    def quitApplication(self):
        self.nextScreen = ScreenString.NONE
        self.changeScreen = True
    
    def toggleDebug(self):
        self.config.debug = not self.config.debug
        sleep(0.1)
    
    def toggleFullscreen(self):
        self.config.fullscreen = not self.config.fullscreen
        sleep(0.1)
    
    def toggleAutoEatFoodInInventory(self):
        self.config.autoEatFoodInInventory = not self.config.autoEatFoodInInventory
        sleep(0.1)
    
    def drawMenuButtons(self):
        # draw buttons in red or green depending on config option value
        # config options to include: debug, fullscreen, autoEatInInventory
        x, y = self.graphik.getGameDisplay().get_size()
        width = x/2
        height = y/10
        # start at top of screen
        xpos = x/2 - width/2
        ypos = 0 + height/2
        margin = 10
        color = (0,255,0) if self.config.debug else (255,0,0)
        self.graphik.drawButton(xpos, ypos, width, height, (255,255,255), color, 30, "debug", self.toggleDebug)
        ypos = ypos + height + margin
        color = (0,255,0) if self.config.fullscreen else (255,0,0)
        self.graphik.drawButton(xpos, ypos, width, height, (255,255,255), color, 30, "fullscreen", self.toggleFullscreen)
        ypos = ypos + height + margin
        color = (0,255,0) if self.config.autoEatFoodInInventory else (255,0,0)
        self.graphik.drawButton(xpos, ypos, width, height, (255,255,255), color, 30, "auto eat in inventory", self.toggleAutoEatFoodInInventory)

        self.drawBackButton()

    def drawBackButton(self):
        # draw in bottom right corner
        x, y = self.graphik.getGameDisplay().get_size()
        width = x/3
        height = y/10
        xpos = x/2 - width/2
        ypos = y/2 - height/2 + width
        self.graphik.drawButton(xpos, ypos, width, height, (255,255,255), (0,0,0), 30, "back", self.switchToMainMenuScreen)

    def run(self):        
        while not self.changeScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return ScreenString.NONE
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyDownEvent(event.key)         
    
            self.graphik.getGameDisplay().fill((0, 0, 0))
            self.drawMenuButtons()
            pygame.display.update()
            
        self.changeScreen = False
        return self.nextScreen