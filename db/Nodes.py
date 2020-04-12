from py2neo import Node

from Relationships import AppearsOn, Has, Creates


class Track(Node):
    # TODO figure out how to incorporate features

    type = "track"

    def __init__(self):
        # TODO figure out what params to expect
        self.name = ""
        self.href = ""
        self.id = ""
        self.uri = "spotify:" + self.type + ":" + self.id
        self.duration_ms = 0
        self.explicit = False
        self.is_local = False
        self.popularity = 0
        self.track_number = 1
        self.albums = []  # TODO create Album objects and store here
        self.artists = []  # TODO create Artist objects and store here

    def as_graph_node(self):
        return Node(type, name=self.name, href=self.href, id=self.id, uri=self.uri, duration_ms=self.duration_ms,
                    explicit=self.explicit, is_local=self.is_local, popularity=self.popularity,
                    track_number=self.track_number)

    def commit_to_graph(self, tx):
        # FIXME make sure duplicate node is not being added
        tx.create(self.as_graph_node())
        for artist in self.artists:  # create Relationship: Artist CREATES Track
            artist.commit_to_graph(tx)  # FIXME add param artist first?
            tx.create(Creates(artist, self).as_graph_edge())
        for album in self.albums:  # create Relationship: Track APPEARS_ON Album
            album.commit_to_graph(tx)  # FIXME add param album first?
            tx.create(AppearsOn(self, album).as_graph_edge())


class Album(Node):

    type = "album"

    def __init__(self):
        # TODO figure out what params to expect
        self.name = ""
        self.href = ""
        self.id = ""
        self.uri = "spotify:" + self.type + ":" + self.id
        self.album_type = ""
        self.release_date = ""  # yyyy-mm-dd
        self.release_date_precision = ""  # e.g., "day"
        self.total_tracks = 0
        self.artists = []  # TODO create Artist objects and store here

    def as_graph_node(self):
        return Node(type, name=self.name, href=self.href, id=self.id, uri=self.uri, album_type=self.album_type,
                    release_date=self.release_date, release_date_precision=self.release_date_precision,
                    total_tracks=self.total_tracks)

    def commit_to_graph(self, tx):
        # FIXME make sure duplicate node is not being added
        tx.create(self.as_graph_node())
        for artist in self.artists: # create Relationship: Album HAS Artist
            tx.create(Has(self, artist).as_graph_edge())


class Artist(Node):

    type = "artist"

    def __init__(self):
        # TODO figure out what params to expect
        self.name = ""
        self.href = ""
        self.id = ""
        self.uri = "spotify:" + self.type + ":" + self.id

    def as_graph_node(self):
        return Node(type, name=self.name, href=self.href, id=self.id, uri=self.uri)

    def commit_to_graph(self, tx):
        # FIXME make sure duplicate node is not being added
        tx.create(self)
