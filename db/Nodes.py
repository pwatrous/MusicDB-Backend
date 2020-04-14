from py2neo import Node, Graph, NodeMatcher

import auth
import getTrackFeatures as tf
import Relationships as rel


graph = Graph("bolt://localhost:7687", user=auth.user, password=auth.password)


def node_exists(label, node):
    matcher = NodeMatcher(graph)
    match = matcher.match(label, id=node["id"]).first()
    return match


def main():

    tx = graph.begin()  # creates a transaction

    tracks = [{'name': 'Muddy Blunts', 'href': 'https://api.spotify.com/v1/tracks/0MsOQYWpwActqMERHaQ3Yg', 'id': '0MsOQYWpwActqMERHaQ3Yg', 'duration_ms': 187454, 'explicit': True, 'is_local': False, 'popularity': 61, 'track_number': 2, 'album': '$outh $ide $uicide', 'artists': ['1VPmR4DJC1PlOtd0IADAO0', '4nXOZlYoAD67hF9aUEncMY']}, {'name': 'Stick Out', 'href': 'https://api.spotify.com/v1/tracks/0jakaHRU7ubOzJTseh6tJu', 'id': '0jakaHRU7ubOzJTseh6tJu', 'duration_ms': 135731, 'explicit': True, 'is_local': False, 'popularity': 61, 'track_number': 1, 'album': 'Stick Out', 'artists': ['4nXOZlYoAD67hF9aUEncMY', '3uL4UpqShC4p2x1dJutoRW']}, {'name': '$outh $ide $uicide', 'href': 'https://api.spotify.com/v1/tracks/4VsMart0lkjUtyQnmxloK6', 'id': '4VsMart0lkjUtyQnmxloK6', 'duration_ms': 169319, 'explicit': True, 'is_local': False, 'popularity': 69, 'track_number': 3, 'album': "High Tide In The Snake's Nest", 'artists': ['1VPmR4DJC1PlOtd0IADAO0']}, {'name': 'ball w/o you', 'href': 'https://api.spotify.com/v1/tracks/4UW4GsTVETXP2mzXfMT2iC', 'id': '4UW4GsTVETXP2mzXfMT2iC', 'duration_ms': 195046, 'explicit': True, 'is_local': False, 'popularity': 56, 'track_number': 10, 'album': 'i am > i was (Deluxe)', 'artists': ['1URnnhqYAYcrqrcwql10ft']}, {'name': 'New Malcolm X', 'href': 'https://api.spotify.com/v1/tracks/2iFT3Gw37kidpE0EkVAZDf', 'id': '2iFT3Gw37kidpE0EkVAZDf', 'duration_ms': 361410, 'explicit': False, 'is_local': False, 'popularity': 45, 'track_number': 3, 'album': 'Better Safe Than Sy Ari', 'artists': ['5ZI5pbnKxA6Qy1fVNsjCp0']}, {'name': "Milk N' Honey", 'href': 'https://api.spotify.com/v1/tracks/72TpOdSgTcuE8IJ0xXz8T6', 'id': '72TpOdSgTcuE8IJ0xXz8T6', 'duration_ms': 258272, 'explicit': True, 'is_local': False, 'popularity': 47, 'track_number': 2, 'album': 'Venice', 'artists': ['3jK9MiCrA42lLAdMGUZpwa']}, {'name': 'I Got 5 On It', 'href': 'https://api.spotify.com/v1/tracks/4IYKjN1DrYzxKXt0umJqsG', 'id': '4IYKjN1DrYzxKXt0umJqsG', 'duration_ms': 253533, 'explicit': False, 'is_local': False, 'popularity': 73, 'track_number': 3, 'album': 'Operation Stackola', 'artists': ['3z3g65U7mmyyBmmDfsQK9x']}, {'name': 'Happiness Over Everything (H.O.E.) (feat. Future & Miguel)', 'href': 'https://api.spotify.com/v1/tracks/2yUy5eFAFWAichjrySJWA2', 'id': '2yUy5eFAFWAichjrySJWA2', 'duration_ms': 188160, 'explicit': False, 'is_local': False, 'popularity': 72, 'track_number': 7, 'album': 'Chilombo', 'artists': ['5ZS223C6JyBfXasXxrRqOk']}, {'name': 'Sativa', 'href': 'https://api.spotify.com/v1/tracks/2pg2TiYo9Rb8KeB5JjP7jS', 'id': '2pg2TiYo9Rb8KeB5JjP7jS', 'duration_ms': 276960, 'explicit': True, 'is_local': False, 'popularity': 75, 'track_number': 7, 'album': 'Trip', 'artists': ['5ZS223C6JyBfXasXxrRqOk']}, {'name': 'Lord Above', 'href': 'https://api.spotify.com/v1/tracks/7q0VdsXafFQIYfk3eZpwTq', 'id': '7q0VdsXafFQIYfk3eZpwTq', 'duration_ms': 294774, 'explicit': True, 'is_local': False, 'popularity': 57, 'track_number': 8, 'album': 'Family Ties', 'artists': ['3ScY9CQxNLQei8Umvpx5g6', '2YKqI0pz6dY15GpzxT66HD']}, {'name': 'Fuck A Hoe - Part II', 'href': 'https://api.spotify.com/v1/tracks/6mWteWfaPFaOCSvVrt42f9', 'id': '6mWteWfaPFaOCSvVrt42f9', 'duration_ms': 191889, 'explicit': True, 'is_local': False, 'popularity': 43, 'track_number': 3, 'album': 'G.R.E.Y.G.O.D.S.', 'artists': ['1VPmR4DJC1PlOtd0IADAO0', '3H6CaRooDAoCeRCpYwOXj2']}, {'name': 'Monkey Wrench', 'href': 'https://api.spotify.com/v1/tracks/4hkD2vPR5deOTrRNcZASbU', 'id': '4hkD2vPR5deOTrRNcZASbU', 'duration_ms': 153450, 'explicit': True, 'is_local': False, 'popularity': 45, 'track_number': 1, 'album': 'Monkey Wrench', 'artists': ['1qHkWv9sHlhqmNdPbMU5tN']}, {'name': 'Let Me Know (I Wonder Why Freestyle)', 'href': 'https://api.spotify.com/v1/tracks/3wwo0bJvDSorOpNfzEkfXx', 'id': '3wwo0bJvDSorOpNfzEkfXx', 'duration_ms': 215380, 'explicit': True, 'is_local': False, 'popularity': 80, 'track_number': 1, 'album': 'Let Me Know (I Wonder Why Freestyle)', 'artists': ['4MCBfE4596Uoi2O4DtmEMz']}, {'name': 'In My White Tee', 'href': 'https://api.spotify.com/v1/tracks/2c5NNtO4efNdwaAE8r41bu', 'id': '2c5NNtO4efNdwaAE8r41bu', 'duration_ms': 129613, 'explicit': True, 'is_local': False, 'popularity': 52, 'track_number': 1, 'album': 'In My White Tee', 'artists': ['6aiFCgyKNwF9Rv5TOxnE8E']}, {'name': 'Rembrandt...Run It Back (with JID & J. Cole feat. Vince Staples)', 'href': 'https://api.spotify.com/v1/tracks/1zJ7ymdM0xajHw4ZYLICBo', 'id': '1zJ7ymdM0xajHw4ZYLICBo', 'duration_ms': 151826, 'explicit': True, 'is_local': False, 'popularity': 50, 'track_number': 13, 'album': "Revenge Of The Dreamers III: Director's Cut", 'artists': ['1iNqsUDUraNWrj00bqssQG', '6l3HvQ5sa6mXTsMTB19rO5']}, {'name': 'QUARANTINE CLEAN', 'href': 'https://api.spotify.com/v1/tracks/4wC5Mudt8Q6rjjnsgX1gas', 'id': '4wC5Mudt8Q6rjjnsgX1gas', 'duration_ms': 217728, 'explicit': False, 'is_local': False, 'popularity': 54, 'track_number': 1, 'album': 'QUARANTINE CLEAN', 'artists': ['002HSjuWsGMinkXTa7JcRp', '2hlmm7s2ICUX0LVIhVFlZQ', '50co4Is1HCEo8bhOyUWKpn']}, {'name': "I Was Sad Last Night I'm OK Now", 'href': 'https://api.spotify.com/v1/tracks/0gEcmyKlIUoi3sHTFVO1bE', 'id': '0gEcmyKlIUoi3sHTFVO1bE', 'duration_ms': 190560, 'explicit': True, 'is_local': False, 'popularity': 63, 'track_number': 3, 'album': 'Live on Ice', 'artists': ['4T8NIfZmVY6TJFqVzN6X49']}, {'name': 'FIND MY WAY', 'href': 'https://api.spotify.com/v1/tracks/1lGHa2pwYzxQHFBUynhLtO', 'id': '1lGHa2pwYzxQHFBUynhLtO', 'duration_ms': 139890, 'explicit': True, 'is_local': False, 'popularity': 86, 'track_number': 1, 'album': 'FIND MY WAY', 'artists': ['4r63FhuTkUYltbVAg5TQnk']}, {'name': 'Special', 'href': 'https://api.spotify.com/v1/tracks/22JMR1yTJBzSVzfkyhpKUV', 'id': '22JMR1yTJBzSVzfkyhpKUV', 'duration_ms': 255712, 'explicit': False, 'is_local': False, 'popularity': 43, 'track_number': 1, 'album': 'Special', 'artists': ['07IN4tO2u845nv3vGkIIIM']}, {'name': 'NOT TOO DEEP (feat. 6LACK)', 'href': 'https://api.spotify.com/v1/tracks/2u925ft5mxwxYLhMQ7Sr72', 'id': '2u925ft5mxwxYLhMQ7Sr72', 'duration_ms': 288412, 'explicit': True, 'is_local': False, 'popularity': 55, 'track_number': 1, 'album': 'NOT TOO DEEP (feat. 6LACK)', 'artists': ['7g0SC4F149FUX5rKFuSpqL', '4IVAbR2w4JJNJDDRFP3E83']}]

    track_features = tf.getSongFeaturesFromIDs(tf.getSongIDs(tracks))

    for track in tracks:
        track_obj = Track(track, track_features[track["id"]])
        if node_exists("Track", track_obj) is None:  # track does not already exist in graph
            track_obj.commit_to_graph(tx)  # FIXME add param track first?

    tx.commit()  # commits the transaction


class Track(Node):

    def __init__(self, prop, features):
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

        print(prop) # TODO remove
        self.albums = Album(prop["album"])

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
        tx.create(self.as_graph_node())
        tx.process()

        for artist in self.artists:  # create Relationship: Artist CREATES Track
            if node_exists("Artist", artist) is None:
                artist.commit_to_graph(tx)  # FIXME add param artist first?
            tx.create(rel.Creates(artist, self).as_graph_edge())
        for album in self.albums:  # create Relationship: Track APPEARS_ON Album
            if node_exists("Album", album) is None:
                album.commit_to_graph(tx)  # FIXME add param album first?
            tx.create(rel.AppearsOn(self, album).as_graph_edge())


class Album(Node):

    def __init__(self, prop):
        self.node_type = "Album"
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + self.node_type.lower() + ":" + self.id
        self.album_type = prop["album_type"]
        self.release_date = prop["release_date"]  # yyyy-mm-dd
        self.release_date_precision = prop["release_date_precision"]  # e.g., "day"
        self.total_tracks = prop["total_tracks"]

        self.artists = []

        for artist in prop["artists"]:
            self.artists.append(Artist(artist))

    def as_graph_node(self):
        return Node(self.node_type, name=self.name, href=self.href, id=self.id, uri=self.uri, album_type=self.album_type,
                    release_date=self.release_date, release_date_precision=self.release_date_precision,
                    total_tracks=self.total_tracks)

    def commit_to_graph(self, tx):
        tx.create(self.as_graph_node())
        tx.proces()

        for artist in self.artists:  # create Relationship: Album HAS Artist
            if node_exists("Artist", artist) is None:
                tx.create(rel.Has(self, artist).as_graph_edge())


class Artist(Node):

    def __init__(self, prop):
        self.node_type = "Artist"
        self.name = prop["name"]
        self.href = prop["href"]
        self.id = prop["id"]
        self.uri = "spotify" + self.node_type.lower() + ":" + self.id

    def as_graph_node(self):
        return Node(self.node_type, name=self.name, href=self.href, id=self.id, uri=self.uri)

    def commit_to_graph(self, tx):
        tx.create(self)
        tx.process()

main()