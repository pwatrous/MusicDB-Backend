import json

input_file = open ('./songs1.json')
json_array = json.load(input_file)
artist_list = []
album_list = []
song_list = []

for item in json_array:
    artist_details = {"name":None, "href":None, "id":None}
    album_details = {"name":None, "href":None, "id":None, "album":None, 
                     "release_date":None, "release_date_precision":None, "total_tracks":None,
                     "artists":None}
    song_details = {"name":None, "href":None, "id":None, "duration_ms":None, "explicit":None,
                    "is_local":None, "popularity":None, "track_number":None, "albums":None, "artists":None}

    for artist in item["track"]["artists"]:
      artist_details["name"] = artist["name"]
      artist_details["href"] = artist["href"]
      artist_details["id"] = artist["id"]
      artist_list.append(artist_details)

print(artist_list)