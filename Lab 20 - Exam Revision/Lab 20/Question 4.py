def categorize_marks_by_range(filename, number_of_ranges):
    try:
        # Open the file and read the marks
        with open(filename, 'r') as file:
            marks = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return {}
    except Exception as e:
        print(f"ERROR: {e}")
        return {}
    else:
        # Calculate the range size based on the number_of_ranges
        range_size = 100 // number_of_ranges
        ranges = {i * range_size: [] for i in range(number_of_ranges)}

        # Categorize each mark
        for mark in marks:
            # Find which range the mark belongs to
            for lower_bound in ranges:
                upper_bound = lower_bound + range_size - 1
                if lower_bound <= mark <= upper_bound:
                    ranges[lower_bound].append(mark)
                    break

        # Sort the marks in each range
        for key in ranges:
            ranges[key].sort()

        return ranges  # Ensure that we return the dictionary