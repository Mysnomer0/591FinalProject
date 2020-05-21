import sys
import os
from scipy.io import wavfile
import contextlib
import pygame

#def playSoundclip(character, stream):


# This function displays the image 'synthImage.jpg' to the game display. This image has the instructions for using the keyboard.
def displayGraphics():
    width = 750
    height = 453
    white = (255, 255, 255)
    x = (width * 0.45)
    y = (height * 0.8)
    gameDisplay = pygame.display.set_mode((width, height))
    gameDisplay.fill(white)
    image = pygame.image.load('synthImage.jpg')
    gameDisplay.blit(image, (0, 0))
    pygame.display.flip()

# This function gets the input from the keyboard until the user presses 'esc'
def keyboardInput():
    while True:
        press = pygame.event.wait()
        if press.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(press.key)
        if press.type == pygame.KEYDOWN:
            if press.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                print("keydown")
        if press.type == pygame.KEYUP:
            print("keyup")
        
        x, y = pygame.mouse.get_rel()
        print(x)


def main():
    # initializing the game
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

    pygame.init()
    displayGraphics()

    #filename = "pianoSample1.wav"
    #fps, sound = wavfile.read(filename)
    #pygame.mixer.pre_init(fps, size=-16, channels=2)
    #pygame.mixer.init()
    #soundArray = pygame.sndarray.make_sound(sound)
    #soundArray.play()
    keyboardInput()


if __name__ == '__main__':
    main()
