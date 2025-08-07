from queue import Queue

class MP3Player:
    def __init__(self):
        self.music_que = Queue()
        self.current_song = ""

    def add_song(self, song):
        self.music_que.appendQueue(song)
        self.current_song = self.music_que.printQueue()[0]

    def play_next_song(self):
        self.music_que.removeQueue()
        self.current_song = self.music_que.printQueue()[0]

    def skip_song(self):
        skippedSong = self.music_que.removeQueue()
        print(skippedSong + " has been skipped")
        self.current_song = self.music_que.printQueue()[0]

    def show_playlist(self):
        return "Current playlist: " + ', '.join(self.music_que.printQueue())
    
    def show_current_song(self):
        return "Now playing: " + self.current_song

newPlaylist = MP3Player()

newPlaylist.add_song("Hello")
newPlaylist.add_song("Never Gonna Give You Up")
newPlaylist.add_song("Bohemian Rhapsody")
newPlaylist.add_song("Thien Ly Oi")
newPlaylist.add_song("That Duc")

print(newPlaylist.show_playlist())
print(newPlaylist.show_current_song())

newPlaylist.play_next_song()

print(newPlaylist.show_playlist())
print(newPlaylist.show_current_song())

newPlaylist.skip_song()

print(newPlaylist.show_playlist())
print(newPlaylist.show_current_song())