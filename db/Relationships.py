from py2neo import Relationship

from Nodes import Track, Album, Artist


class AppearsOn(Relationship):

    def __init__(self, track, album):
        if not isinstance(track, Track):
            print("Appears_On: expected Track; given " + track)
        elif not isinstance(album, Album):
            print("Appears_On: expected Album; given " + album)


class Has(Relationship):

    def __init__(self, album, artist):
        if not isinstance(album, Album):
            print("Has: expected Album; given " + album)
        elif not isinstance(artist, Artist):
            print("Has: expected Artist; given " + artist)


class Creates(Relationship):

    def __init__(self, artist, track):
        if not isinstance(artist, Artist):
            print("Creates: expected Artist; given " + artist)
        elif not isinstance(track, Track):
            print("Creates: expected Track; given " + track)
