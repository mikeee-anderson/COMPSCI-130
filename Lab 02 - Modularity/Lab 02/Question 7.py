regions_dict = {'Kaitaia': [110.0, 11.766666666666666], 'Auckland': [93.24166666666667, 12.058333333333335], 'Tauranga': [100.125, 10.841666666666667]}
def print_table(regions_dict, column_names):
    print("            Name|    Rainfall(mm)| Min.Temperature|")
    for key, value in sorted(regions_dict.items()):
        print(f"{key:>16}|{round(value[0], 2):>16.2f}|{round(value[1],2):>16}|")



print_table(regions_dict, ['Rainfall(mm)', 'Min.Temperature'])