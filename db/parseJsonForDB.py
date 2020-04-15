import json

def parse(path):
    input_file = open(path)
    json_array = json.load(input_file)
    artist_list = []
    album_list = []
    song_list = []

    for item in json_array:
        artist_details = {"name":None, "href":None, "id":None}
        album_details = {"name":None, "href":None, "id":None, "album_type":None,
                         "release_date":None, "release_date_precision":None, "total_tracks":None,
                         "artists":[]}
        song_details = {"name":None, "href":None, "id":None, "duration_ms":None, "explicit":None,
                        "is_local":None, "popularity":None, "track_number":None, "album":[], "artists":[]}

        for artist in item["track"]["artists"]:
            artist_details["name"] = artist["name"]
            artist_details["href"] = artist["href"]
            artist_details["id"] = artist["id"]
            artist_list.append(artist_details)

        album_details["name"] = item["track"]["album"]["name"]
        album_details["href"] = item["track"]["album"]["href"]
        album_details["id"] = item["track"]["album"]["id"]
        album_details["album_type"] = item["track"]["album"]["album_type"]
        album_details["release_date"] = item["track"]["album"]["release_date"]
        album_details["release_date_precision"] = item["track"]["album"]["release_date_precision"]
        album_details["total_tracks"] = item["track"]["album"]["total_tracks"]

        for artist in item["track"]["album"]["artists"]:
            artist_details["name"] = artist["name"]
            artist_details["href"] = artist["href"]
            artist_details["id"] = artist["id"]
            album_details["artists"].append(artist_details)

        album_list.append(album_details)

        song_details["name"] = item["track"]["name"]
        song_details["href"] = item["track"]["href"]
        song_details["id"] = item["track"]["id"]
        song_details["duration_ms"] = item["track"]["duration_ms"]
        song_details["explicit"] = item["track"]["explicit"]
        song_details["is_local"] = item["track"]["is_local"]
        song_details["popularity"] = item["track"]["popularity"]
        song_details["track_number"] = item["track"]["track_number"]
        song_details["album"] = album_details

        for artist in item["track"]["album"]["artists"]:
            artist_details["name"] = artist["name"]
            artist_details["href"] = artist["href"]
            artist_details["id"] = artist["id"]
            song_details["artists"].append(artist_details)

        song_list.append(song_details)

    return song_list
