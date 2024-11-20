class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_disks = [0] * size
        self.items = [[0] * size for _ in range(size)]
        self.points = [0] * 2  # Points for Player 1 and Player 2

    def display(self):
        for row in range(self.size - 1, -1, -1):  # Iterate from top to bottom
            row_display = ""
            for col in range(self.size):
                if self.items[col][row] == 0:
                    row_display += " "  # Empty space
                elif self.items[col][row] == 1:
                    row_display += "o"  # Player 1
                elif self.items[col][row] == 2:
                    row_display += "x"  # Player 2
                if col < self.size - 1:
                    row_display += " "  # Space between columns
            print(row_display)

        print("-" * (2 * self.size - 1))  # Separator line
        print(" ".join(str(i) for i in range(self.size)))  # Column numbers
        print(f"Points player 1: {self.points[0]}")
        print(f"Points player 2: {self.points[1]}")

    def num_new_points(self, column, row, player):
        new_points = 0

        # Check in all four directions: horizontal, vertical, diagonal / and diagonal \
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        for delta_col, delta_row in directions:
            count1 = 0
            count2 = 0

            # Count in the positive direction
            c, r = column, row
            while 0 <= c < self.size and 0 <= r < self.size and self.items[c][r] == player:
                count1 += 1
                c += delta_col
                r += delta_row

            # Count in the negative direction
            c, r = column, row
            while 0 <= c < self.size and 0 <= r < self.size and self.items[c][r] == player:
                count2 += 1
                c -= delta_col
                r -= delta_row

            # Total count is the counts from both directions minus 1 for the current piece
            total_count = count1 + count2 - 1

            # If we have at least 4, it's a valid sequence
            if total_count >= 4:
                new_points += 1  # Increment the point count for each new 4-in-a-row found

        return new_points

    def add(self, column, player):
        if column < 0 or column >= self.size:
            return False  # Invalid column
        if self.num_disks[column] >= self.size:
            return False  # Column full

        row = self.num_disks[column]  # Get the next available row
        self.items[column][row] = player  # Place the player's disk
        self.num_disks[column] += 1  # Increment the disk count in the column

        # Calculate new points based on the last move
        new_points = self.num_new_points(column, row, player)
        self.points[player - 1] += new_points  # Update player's points

        return True



# Test case
board = GameBoard(5)
board.add(0, 1)
board.add(0, 2)
board.add(1, 1)
board.add(1, 2)
board.add(3, 1)
board.add(3, 2)
board.add(4, 1)
board.add(4, 2)
board.add(2, 1)
print("Newly created 4-in-a-row sequences: ", board.num_new_points(2, 0, 1))
board.display()