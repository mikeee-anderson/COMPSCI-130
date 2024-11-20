def get_total_duration_for_artist(song_dictionary, artist):
    try:
            songs = song_dictionary[artist]
            duration = 0
            for song in songs:
                try:
                    time = song[1]
                    duration += time
                except IndexError:
                    print(f"ERROR: Missing the duration in '{song[0]}'.")
                    break
            return duration
    except KeyError:
        print(f"ERROR: '{artist}' is not available.")
        return 0

    except TypeError:
        print(f"ERROR: Invalid input!")
        return 0

song_dict = {'Wiz Khalifa': [('Say Yeah',241), ('Something New', 200), ('See You Again', ), ('We Own It',227)], 'Mark Ronson': [('Uptown Funk', 270)], 'PSY': [('Gangnam Style', 219), ('New Face', 190)]}
print(get_total_duration_for_artist(song_dict, 'PSY'))
print(get_total_duration_for_artist(song_dict, 'Taylor Swift'))
print(get_total_duration_for_artist(song_dict, [123]))
print(get_total_duration_for_artist(song_dict, 'Wiz Khalifa'))