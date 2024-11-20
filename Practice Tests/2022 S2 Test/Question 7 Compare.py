def get_total_duration_for_artist(song_dictionary, artist):
    if not isinstance(song_dictionary, dict):
        print("ERROR: The song dictionary is invalid!")
        return 0

    try:
        songs = song_dictionary[artist]
    except KeyError:
        print(f"ERROR: '{artist}' is not available.")
        return 0

    duration = 0
    for song in songs:
        if len(song) < 2:
            print(f"ERROR: Missing the duration in '{song[0]}'.")
            continue
        try:
            time = song[1]
            if not isinstance(time, (int, float)):  # Check if duration is a number
                raise TypeError
            duration += time
        except TypeError:
            print(f"ERROR: Invalid duration format in '{song[0]}'.")

    return duration

song_dict = {'Wiz Khalifa': [('Say Yeah',241), ('Something New', 200), ('See You Again', ), ('We Own It',227)], 'Mark Ronson': [('Uptown Funk', 270)], 'PSY': [('Gangnam Style', 219), ('New Face', 190)]}
print(get_total_duration_for_artist(song_dict, 'PSY'))
print(get_total_duration_for_artist(song_dict, 'Taylor Swift'))
print(get_total_duration_for_artist(song_dict, [123]))
print(get_total_duration_for_artist(song_dict, 'Wiz Khalifa'))