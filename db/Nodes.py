from py2neo import Node, Graph, NodeMatcher

import auth
import parseJsonForDB as ps
import getTrackFeatures as tf
import Relationships as rel


graph = Graph("bolt://localhost:7687", user=auth.user, password=auth.password)

def main():

    tx = graph.begin()  # creates a transaction

    path = './songs1.json'

    tracks = ps.parse(path)

    track_features = tf.getSongFeaturesFromIDs(tf.getSongIDs(tracks))

    for track in tracks:
        if track_features.has_key(track["id"]):
            track_obj = Track(track, track_features[track["id"]])
            if node_exists("Track", track_obj) is None:  # track does not already exist in graph
                track_obj.commit_to_graph(tx)

    tx.commit()  # commits the transaction


def node_exists(label, node):
    matcher = NodeMatcher(graph)
    return matcher.match(label, name=node.name).first()


#Every track will have a list of feature, and we can use this list of feature to find similar tracks that are produced by other artists
#Feature()
#For every tracks that this user liked, we run this query with this track and other tracks produced by the same artist
#Expected output: The similarity between every tracks in the list.
#We will take the top 2 - 3 songs that has the highest similarity to this track, and recommend it to the user
#In the future, we can run this query on a larger range of tracks to improve the performance
#For now, due to the technical error, we are not able to run gds.alpha.ml.ann.stream
def songRecommendation():
    query = "MATCH (a:Track)-[:Has]->(feature:Feature)"\
    "WITH {item:id(a), categories: collect(id(Feature))} AS userData"\
    "WITH collect(userData) AS data"\
    "CALL gds.alpha.ml.ann.stream({"\
    "nodeProjection: '*',"\
    "relationshipProjection: '*',"\
    "data: data,"\
    "algorithm: 'jaccard',"\
    "similarityCutoff: 0.1,"\
    "concurrency: 1"\
    "})"\
    "YIELD item1, item2, similarity"\
    "return gds.util.asNode(item1).name AS from, gds.util.asNode(item2).name AS to, similarity"\
    "ORDER BY from"
    result = graph.run(query)
    return result




class Track(Node):

    def __init__(self, prop, features):
        # track properties
        self.node_type = "Track"
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + self.node_type.lower() + ":" + self.id
        self.duration_ms = prop["duration_ms"]
        self.explicit = prop["explicit"]
        self.is_local = prop["is_local"]
        self.popularity = prop["popularity"]
        self.track_number = prop["track_number"]
        # audio features
        self.energy = features["energy"]
        self.liveness = features["liveness"]
        self.tempo = features["tempo"]
        self.speechiness = features["speechiness"]
        self.acousticness = features["acousticness"]
        self.instrumentalness = features["instrumentalness"]
        self.time_signature = features["time_signature"]
        self.danceability = features["danceability"]
        self.key = features["key"]
        self.loudness = features["loudness"]
        self.valence = features["valence"]
        self.mode = features["mode"]
        # album
        self.album = Album(prop["album"])
        # track artists
        self.artists = []
        for artist in prop["artists"]:
            self.artists.append(Artist(artist))

    def as_graph_node(self):
        return Node(self.node_type,
                    name=self.name, href=self.href, id=self.id, uri=self.uri,
                    duration_ms=self.duration_ms, explicit=self.explicit, is_local=self.is_local,
                    popularity=self.popularity, track_number=self.track_number,
                    energy=self.energy, liveness=self.liveness, tempo=self.tempo, speechiness=self.speechiness,
                    acousticness=self.acousticness, instrumentalness=self.instrumentalness,
                    time_signature=self.time_signature, danceability=self.danceability, key=self.key,
                    loudness=self.loudness, valence=self.valence, mode=self.mode)

    def commit_to_graph(self, tx):
        track_node = self.as_graph_node()
        tx.create(track_node)
        tx.process()

        for artist in self.artists:  # create Relationship: Artist CREATES Track
            artist_match = node_exists("Artist", artist)
            if artist_match is None:
                artist_match = artist.commit_to_graph(tx)
            tx.create(rel.Creates(artist_match, track_node).as_graph_edge())
            tx.process()

        album_match = node_exists("Album", self.album)
        if album_match is None:
            album_match = self.album.commit_to_graph(tx)
        tx.create(rel.AppearsOn(track_node, album_match).as_graph_edge())
        tx.process()


class Album(Node):

    def __init__(self, prop):
        # album properties
        self.node_type = "Album"
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + self.node_type.lower() + ":" + self.id
        self.album_type = prop["album_type"]
        self.release_date = prop["release_date"]  # yyyy-mm-dd
        self.release_date_precision = prop["release_date_precision"]  # e.g., "day"
        self.total_tracks = prop["total_tracks"]
        # album artists
        self.artists = []
        for artist in prop["artists"]:
            self.artists.append(Artist(artist))

    def as_graph_node(self):
        return Node(self.node_type, name=self.name, href=self.href, id=self.id, uri=self.uri, album_type=self.album_type,
                    release_date=self.release_date, release_date_precision=self.release_date_precision,
                    total_tracks=self.total_tracks)

    def commit_to_graph(self, tx):
        album_node = self.as_graph_node()
        tx.create(album_node)
        tx.process()

        for artist in self.artists:  # create Relationship: Album HAS Artist
            artist_match = node_exists("Artist", artist)
            if artist_match is None:
                artist_match = artist.commit_to_graph(tx)
            tx.create(rel.Has(album_node, artist_match).as_graph_edge())
            tx.process()

        return album_node


class Artist(Node):

    def __init__(self, prop):
        # artist properties
        self.node_type = "Artist"
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + self.node_type.lower() + ":" + self.id

    def as_graph_node(self):
        return Node(self.node_type, name=self.name, href=self.href, id=self.id, uri=self.uri)

    def commit_to_graph(self, tx):
        artist_node = self.as_graph_node()
        tx.create(artist_node)
        tx.process()
        return artist_node

main()
