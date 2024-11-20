class Rainfall:
    def __init__(self, location="UNKNOWN"):
        self.location = location
        self.monthly_rainfall_list = []
    def add_rainfall(self, measurement):
        self.monthly_rainfall_list.append(measurement)
    def get_annual_rainfall(self):
        total = 0
        for i in self.monthly_rainfall_list:
            total += i
        return total
    def get_average_monthly_rainfall(self):
        count = 0
        total = 0
        for data in self.monthly_rainfall_list:
            total += data
            count += 1
        average = total / count
        return average
    def __str__(self):
        if not self.monthly_rainfall_list:
            return "No rainfall data for {}".format(self.location)
        else:
            average_rainfall = self.get_average_monthly_rainfall()
            return "Location: {}, Average Monthly Rainfall: {:.2f} mm".format(self.location, average_rainfall)

region1 = Rainfall()
auckland = Rainfall('Auckland')
rainfall_data = [75.3, 62.0, 88.7, 120.5, 135.2, 98.6, 112.4, 140.0, 85.6, 74.5, 64.3, 90.2]
for value in rainfall_data:
    auckland.add_rainfall(value)
print(auckland)
print(auckland.get_annual_rainfall())
print(type(auckland))
print(auckland)
print(region1)
print(auckland.get_annual_rainfall())