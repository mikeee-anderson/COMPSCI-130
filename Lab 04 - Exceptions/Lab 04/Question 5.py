data_dict = {'a':'q', 'd':'a', 'e':'f', 'q':None, 'f':'o', 'g':'h', 'h':'m'}
def get_connected_list(airports_dict, start_airport):
    try:
        journey_list = []
        while airports_dict[start_airport] != None:
            journey_list.append(start_airport)
            start_airport = airports_dict[start_airport]
        journey_list.append(start_airport)
        return (journey_list, 'Success!')
    except KeyError:
        journey_list.append(start_airport)
        return(journey_list, 'Missing end destination')




print(get_connected_list(data_dict, 'd'))
result = get_connected_list(data_dict, 'f')
print(type(result), result)