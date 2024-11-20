regions_dict = {'Auckland':[93.24], 'Hamilton':[] }
data_dict = {'Auckland': [16.2, 16.6, 14.2, 12.2, 10.8, 8.2, 7.2, 8.2, 9.2, 11]}
def merge_data(regions_dict, data_dict):
    for key in data_dict:
        total_data = sum(data_dict[key])
        number_of_points = len(data_dict[key])
        average = round(total_data / number_of_points, 2)
        regions_dict[key].append(average)
    return regions_dict


merge_data(regions_dict, data_dict)
for key in sorted(regions_dict):
    print(key, regions_dict[key])