# Multiple methods

class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
        print(f"added:{song}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"removed:{song}")
    def show_songs(self):
        print(f"Playlist:{self.name}")
        for i in self.songs:
            print(i)

my_Playlist=Playlist("favorites")
my_Playlist.add_song("Boom Boom")
my_Playlist.add_song("Devara")
my_Playlist.show_songs()

#You can delete methods from a class using the del keyword:

del Playlist.remove_song
# my_Playlist.remove_song("Devara")# This will cause an error
my_Playlist.show_songs()