import pygame
import os

class MusicPlayer:
    def __init__(self, folder="music"):
        pygame.mixer.init()

        # Load all songs
        self.songs = [folder + "/" + f for f in os.listdir(folder) if f.endswith(".mp3")]
        self.index = 0

        # Load first song
        pygame.mixer.music.load(self.songs[self.index])

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def next(self):
        self.index = (self.index + 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()

    def set_volume(self, v):
        pygame.mixer.music.set_volume(v)   # v between 0.0 and 1.0
