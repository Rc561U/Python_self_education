class MediaPlayer:

    def __init__(self):
        self.filename = None

    def open(self, file):
        self.filename = file
        return self.filename

    def play(self):
        return f'Воспроизведение {self.filename}'


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")
print(media1.play())
print(media2.play())