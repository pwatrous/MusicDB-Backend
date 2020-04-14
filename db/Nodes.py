from py2neo import Node, Graph, NodeMatcher
from Relationships import AppearsOn, Has, Creates

import auth


graph = Graph("bolt://localhost:7687", user=auth.user, password=auth.password)


def node_exists(label, node):
    print(type(node))
    matcher = NodeMatcher(graph)
    match = matcher.match(label, id=node["id"]).first()
    return match


def main():

    tx = graph.begin()  # creates a transaction

    tracks = []
    # TODO parse inputs from frontend and fill tracks

    for track in tracks:
        if node_exists("Track", track) is None:  # track does not already exist in graph
            track.commit_to_graph(tx)  # FIXME add param track first?

    tx.commit()  # commits the transaction


class Track(Node):
    # TODO figure out how to incorporate features

    type = "Track"

    def __init__(self, prop):
        # TODO figure out what params to expect
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + type.lower() + ":" + self.id
        self.duration_ms = prop["duration_ms"]
        self.explicit = prop["explicit"]
        self.is_local = prop["is_local"]
        self.popularity = prop["popularity"]
        self.track_number = prop["track_number"]

        # TODO track features

        self.albums = []  # TODO create Album objects and store here
        self.artists = []  # TODO create Artist objects and store here

    def as_graph_node(self):
        return Node(type, name=self.name, href=self.href, id=self.id, uri=self.uri, duration_ms=self.duration_ms,
                    explicit=self.explicit, is_local=self.is_local, popularity=self.popularity,
                    track_number=self.track_number)  # TODO track features

    def commit_to_graph(self, tx):
        tx.create(self.as_graph_node())
        tx.process()

        for artist in self.artists:  # create Relationship: Artist CREATES Track
            if node_exists("Artist", artist) is None:
                artist.commit_to_graph(tx)  # FIXME add param artist first?
            tx.create(Creates(artist, self).as_graph_edge())
        for album in self.albums:  # create Relationship: Track APPEARS_ON Album
            if node_exists("Album", album) is None:
                album.commit_to_graph(tx)  # FIXME add param album first?
            tx.create(AppearsOn(self, album).as_graph_edge())


class Album(Node):

    type = "Album"

    def __init__(self, prop):
        # TODO figure out what params to expect
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + type.lower() + ":" + self.id
        self.album_type = prop["album_type"]
        self.release_date = prop["release_date"]  # yyyy-mm-dd
        self.release_date_precision = prop["release_date_precision"]  # e.g., "day"
        self.total_tracks = prop["total_tracks"]
        self.artists = []  # TODO create Artist objects and store here

    def as_graph_node(self):
        return Node(type, name=self.name, href=self.href, id=self.id, uri=self.uri, album_type=self.album_type,
                    release_date=self.release_date, release_date_precision=self.release_date_precision,
                    total_tracks=self.total_tracks)

    def commit_to_graph(self, tx):
        # FIXME make sure duplicate node is not being added
        tx.create(self.as_graph_node())
        tx.proces()

        for artist in self.artists:  # create Relationship: Album HAS Artist
            if node_exists("Artist", artist) is None:
                tx.create(Has(self, artist).as_graph_edge())


class Artist(Node):

    type = "Artist"

    def __init__(self, prop):
        # TODO figure out what params to expect
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + type.lower() + ":" + self.id

    def as_graph_node(self):
        return Node(type, name=self.name, href=self.href, id=self.id, uri=self.uri)

    def commit_to_graph(self, tx):
        # FIXME make sure duplicate node is not being added
        tx.create(self)
        tx.process()
