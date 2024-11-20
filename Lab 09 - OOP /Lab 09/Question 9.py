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

class RainfallCollection:
    def __init__(self):
        self.rainfall_records = []
    def add_record(self, rainfall_record):
        if rainfall_record.get_annual_rainfall() > 0:
            self.rainfall_records.append(rainfall_record)
    def get_total_annual_rainfall(self):
        total = 0
        for record in self.rainfall_records:
            total += record.get_annual_rainfall()
        return total

    def __str__(self):
        if not self.rainfall_records:
            return "No rainfall records available."
        return "\n".join([str(x) for x in self.rainfall_records])
data1 = RainfallCollection()
region1 = Rainfall('Auckland')
region1.add_rainfall(62.0)
region1.add_rainfall(88.7)
region2 = Rainfall()
data1.add_record(region1)
data1.add_record(region2)
print(data1)
print(data1.get_total_annual_rainfall())
