class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number < other.nhi_number
        return False

    def selection_sort(patients):
        for position in range(len(patients) - 1, 0, -1):
            largest_index = 0
            for index in range(1, position + 1):