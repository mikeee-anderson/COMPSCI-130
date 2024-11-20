dictionary =  {315: 'Kate Edger Information Commons', 303: 'Science building',
  106: 'Biology Building',206: 'Humanities Building',201: 'Social Sciences Building',110: 'Thomas Building'}
def get_building_name(building_dictionary, building_number):
    try:
        building_number = int(building_number)
        return building_dictionary[building_number]
    except ValueError:
        return (f"ERROR: Invalid number!\nNone")
    except KeyError:
        return (f"ERROR: '{building_number}' is not available.\nNone")


print(get_building_name(dictionary, 123))
print(get_building_name(dictionary, 201))
print(get_building_name(dictionary, '206'))
print(get_building_name(dictionary, 'yes'))
