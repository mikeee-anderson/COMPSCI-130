def print_total_durations(song_dictionary):
    sorted_dict = dict(sorted(song_dictionary.items()))
    artists = sorted_dict.keys()

    for artist in artists:
        songs = song_dictionary[artist]
        duration = 0
        for song in songs:
            time = song[1]
            duration += time
        print(f"{artist} {duration}")


song_dict = {'Wiz Khalifa': [('We Own It', 227), ('See You Again', 229)], 'PSY': [('New Face', 190)]}
print_total_durations(song_dict)

