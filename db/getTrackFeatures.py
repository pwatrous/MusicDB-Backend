import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Set environment variables SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
def spotifyAuth():
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    return sp


# These methods should allow the fetching of audio features for songs to get all necessary
#  song information to put into the database.

def getSongIDs(songs):
    '''Given a list of Spotify songs, return a list of their ids'''
    ids = []
    for i in range(len(songs)):
        ids.append(songs[i]['track']['id'])
    return ids

def getSongFeatures(songs):
    '''Given a list of Spotify Songs, return a list of all audio features for each song'''
    # TODO If songs is a list of Spotify Track Objects, then possibly remove '['track']' as it may be unneeded
    # sp is the Spotify Object that makes the api calls
    sp = spotifyAuth()
    songFeatures = []
    songIDs = getSongIDs(songs)
    k = 0
    for i in range(0, len(songIDs), 50):
        audio_features = sp.audio_features(songIDs[i:i+50])
        for track in audio_features:
            if track != None:
                track['id'] = songIDs[k]
                track['song_title'] = songs[k]['track']['name']
                track['artist'] = songs[k]['track']['artists'][0]['name']
                track['trackPopularity'] = songs[k]['track']['popularity']
                songFeatures.append(track)
                k = k + 1
            else:
                break
    # The list songFeatures should contain all necessary information about songs
    # Each entry is a track with the song id, song title, artist, popularity, and its audio features
    return songFeatures

def getSongFeaturesFromIDs(ids):
    '''Given a list of song ids, return a dictionary with ids mapped to song features'''

    sp = spotifyAuth()
    # songFeatures = []
    songFeatures = {}
    k = 0
    for i in range(0, len(ids), 50):
        audio_features = sp.audio_features(ids[i:i+50])
        for track in audio_features:
            if track != None:
                songFeatures[ids[k]] = track
            else:
                break

    return songFeatures