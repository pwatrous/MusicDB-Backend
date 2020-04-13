import json
import pandas as pd
from pandas.io.json import json_normalize
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '403bf1e615234ed6944b99a889501fc4'
secret = '11da18e5e66049ba8a62b703ec4e314c'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# to use recommendations, we need seed_artists(a list of artist IDs, URIs or URLs), seed_genres(a list of genre names.),
# seed_tracks(a list of track IDs, URIs or URLs), limit
# no data about genre in the json file
def getRecommendation(json_file_path,RecPerSong):
    with open(json_file_path) as f:
        data = json.loads(f.read())
    metadata = json_normalize(data)
    column_names = ["track_id","track_name","seed_artists"]
    df = pd.DataFrame(columns = column_names)
    result = []
    for line in range(0,len(metadata)):
        track_id = [metadata["track.id"][line]]
        track_name = metadata["track.name"][line]
        seed_artists = []
        for artist in metadata["track.album.artists"][line]:
            seed_artists.append(artist['id'])
        df = df.append({'track_id' :track_id, 'track_name' : track_name,'seed_artists':seed_artists,} , ignore_index=True)
        for track in range(0,len(df)):
            re = sp.recommendations(seed_artists=df['seed_artists'][track],
                       seed_tracks=df['track_id'][track],
                       limit=RecPerSong)
            result = result+re['tracks']
    column_names = ["track_id","track_name","artists_id","artists_name"]
    re_df = pd.DataFrame(columns = column_names)
    for track in test:
        track_id=track["album"]["id"]
        track_name=track["album"]["name"]
        artists_id=[]
        artists_name=[]
        for artist in track["artists"]:
            artists_id.append(artist["id"])
            artists_name.append(artist["name"])
        re_df = re_df.append({"track_id":track_id,"track_name":track_name,"artists_id":artists_id,"artists_name":artists_name} , ignore_index=True)
    return re_df
