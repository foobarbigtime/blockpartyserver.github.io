import keyboard
import pygame
import os

# Initialize Pygame Mixer
pygame.mixer.init()

# Load the sound file
sound_file = "Keyboard.mp3"
if not os.path.exists(sound_file):
    print(f"Error: {sound_file} not found!")
    exit()

slime_sound = pygame.mixer.Sound(sound_file)

def play_sound(e):
    # Prevents sound from playing on holding down a key
    if e.event_type == 'down':
        # Use play() without blocking to allow rapid clicking
        slime_sound.play()

# Set up the keyboard hook for all keys
keyboard.hook(play_sound)

print("Slime keyboard active. Press 'Esc' to exit.")
# Block until ESC is pressed
keyboard.wait('esc')
