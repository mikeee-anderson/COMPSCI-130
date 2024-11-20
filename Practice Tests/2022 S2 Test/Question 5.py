def create_song_dictionary(songs_list):
    song_dict = {}
    for song in songs_list:
        song_name, artist, duration = song.split(",")
        song_tuple = (song_name, int(duration))
        if artist not in song_dict:
            song_dict[artist] = []
            song_dict[artist].append(song_tuple)
        else:
            song_dict[artist].append(song_tuple)
    return song_dict

songs = ["We Own It,Wiz Khalifa,227", "See You Again,Wiz Khalifa,229", "New Face,PSY,190"]
songs_dict = create_song_dictionary(songs)
for key in sorted(songs_dict):
    print(key, sorted(songs_dict[key]))
print(type(songs_dict))
print(type(songs_dict['Wiz Khalifa']))
print(type(songs_dict['Wiz Khalifa'][0]))