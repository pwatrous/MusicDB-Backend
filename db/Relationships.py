from py2neo import Relationship


class AppearsOn(Relationship):

    def __init__(self, track, album):
        # from Nodes import Track, Album
        # if not isinstance(track, Track):
        #     print("Appears_On: expected Track; given " + track)
        # elif not isinstance(album, Album):
        #     print("Appears_On: expected Album; given " + album)

        self.track = track
        self.album = album

    def as_graph_edge(self):
        return Relationship(self.track, "APPEARS_ON", self.album)


class Has(Relationship):

    def __init__(self, album, artist):
        # from Nodes import Album, Artist
        # if not isinstance(album, Album):
        #     print("Has: expected Album; given " + album)
        # elif not isinstance(artist, Artist):
        #     print("Has: expected Artist; given " + artist)

        self.album = album
        self.artist = artist

    def as_graph_edge(self):
        return Relationship(self.album, "HAS", self.artist)


class Creates(Relationship):

    def __init__(self, artist, track):
        # from Nodes import Track, Artist
        # if not isinstance(artist, Artist):
        #     print("Creates: expected Artist; given " + artist)
        # elif not isinstance(track, Track):
        #     print("Creates: expected Track; given " + track)

        self.artist = artist
        self.track = track

    def as_graph_edge(self):
        return Relationship(self.artist, "CREATES", self.track)
