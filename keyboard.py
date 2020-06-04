import sys
import os
import synthplayer
from scipy.io import wavfile
import contextlib
import pygame
import sounddevice as sd
from synthesizer import Player, Synthesizer, Waveform

frequencyArray = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94,
                  261.63, 277.18, 293.66, 311.13, 329.63]
synthesizer = None
currentOctave = 3

def transposeUp():
    global synthesizer
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, osc2_waveform=Waveform.square, use_osc2=1.0)
    global frequencyArray
    frequencyArray = [i * 2 for i in frequencyArray]
    keyArray = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j', 'k', 'o', 'l', 'p',';']
    soundArray = {}
    for i in range (len(frequencyArray)):
        newSound = synthesizer.generate_constant_wave(frequencyArray[i], length=4)
        soundArray.update({keyArray[i]:newSound})
    keyboardInput(soundArray, keyArray)


def transposeDown():
    global synthesizer
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, osc2_waveform=Waveform.square, use_osc2=1.0)
    global frequencyArray
    frequencyArray = [i / 2 for i in frequencyArray]
    keyArray = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j', 'k', 'o', 'l', 'p',';']
    soundArray = {}
    for i in range (len(frequencyArray)):
        newSound = synthesizer.generate_constant_wave(frequencyArray[i], length=4)
        soundArray.update({keyArray[i]:newSound})
    keyboardInput(soundArray, keyArray)


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
def keyboardInput(soundArray, keyArray):
    isPlaying = {k: False for k in keyArray}
    global currentOctave

    while True:
        press = pygame.event.wait()
        if press.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(press.key)
        if press.type == pygame.KEYDOWN:
            if (key in keyArray) and (not isPlaying[key]):
                sd.play(soundArray[key])
                isPlaying[key] = True
            elif press.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if press.type == pygame.KEYUP:
            sd.stop()
            isPlaying[key] = False

        x, y = pygame.mouse.get_rel()
        if x > 10 and currentOctave < 7:
            currentOctave = currentOctave + 1
            transposeUp()
            keyboardInput(soundArray, keyArray)
        elif x < -10 and currentOctave > 0:
            currentOctave = currentOctave - 1
            transposeDown()
            keyboardInput(soundArray, keyArray)

def main():
    # initializing the game
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    pygame.init()
    displayGraphics()
    pygame.mixer.init(44100, -16, 1, 2048)
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, osc2_waveform=Waveform.square, use_osc2=1.0)
    global frequencyArray
    keyArray = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j', 'k', 'o', 'l', 'p',';']
    soundArray = {}
    for i in range (len(frequencyArray)):
        newSound = synthesizer.generate_constant_wave(frequencyArray[i], length=4)
        soundArray.update({keyArray[i]:newSound})

    keyboardInput(soundArray, keyArray)


if __name__ == '__main__':
    main()
