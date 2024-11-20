def get_cube_volume(length):
    try:
        length = float(length)
        if length > 0:
            volume = round(length ** 3)
            return(volume, '')
        elif length == 0:
            return(0, "ERROR: Not a cube!" )
        else:
            return(0, "ERROR: Length must be positive!")
    except TypeError:
        return(0, "ERROR: The type is incorrect!" )
    except ValueError:
        return(0, "ERROR: The value is invalid!" )

print(get_cube_volume(10.5))
print(get_cube_volume(-1))
print(get_cube_volume(0))
