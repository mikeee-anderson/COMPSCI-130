class DivisibleNumbersIterator:
    def __init__(self, number_of_terms=5, divisor=1):
        self.number_of_terms = number_of_terms  # Number of terms to generate
        self.divisor = divisor  # The divisor
        self.current = divisor  # Start with the first multiple of the divisor
        self.count = 0  # Count of terms generated

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.count < self.number_of_terms:
            result = self.current  # Store the current number to return
            self.current += self.divisor  # Move to the next multiple of the divisor
            self.count += 1  # Increment the count of terms generated
            return result  # Return the current number
        else:
            raise StopIteration  # No more elements to return