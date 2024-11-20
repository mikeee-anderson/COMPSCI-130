class SquareNumberIterator:
    def __init__(self, number_of_squares=5):
        self.number_of_squares = number_of_squares  # Number of square numbers needed
        self.current = 1  # Initialize the current number to 1

    def __next__(self):
        if self.current > self.number_of_squares:
            raise StopIteration  # Stop iteration when the number of squares is reached

        square = self.current ** 2  # Calculate the square of the current number
        self.current += 1  # Move to the next number
        return square  # Return the current square

class SquareNumber:
    def __init__(self, number_of_squares=5):
        self.number_of_squares = number_of_squares

    def __iter__(self):
        return SquareNumberIterator(self.number_of_squares)