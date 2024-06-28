class SoundManager:
    def __init__(self, sound_files):
        # Load sounds from the provided dictionary of sound files
        self.sounds = {}
        for key, file in sound_files.items():
            try:
                self.sounds[key] = pygame.mixer.Sound(file)
            except pygame.error as e:
                print(f"Cannot load sound {file}: {e}")

    def play(self, sound_key):
        # Play the sound associated with the given key
        if sound_key in self.sounds:
            self.sounds[sound_key].play()
        else:
            print(f"Sound {sound_key} not found!")