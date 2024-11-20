data = ['Auckland', 'Hamilton']

def create_regions_dictionary(regions_list):
    regions_dict = {}
    for region in regions_list:
        regions_dict[region] = []
    return regions_dict

a_dict = create_regions_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])