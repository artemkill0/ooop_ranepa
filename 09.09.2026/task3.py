class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")

media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("song1.mp3")
media2.open("song2.mp3")

media1.play()  # Воспроизведение song1.mp3
media2.play()  # Воспроизведение song2.mp3