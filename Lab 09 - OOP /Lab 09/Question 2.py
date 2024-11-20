class Address:
    def __init__(self, street, city, postal_code, is_residential):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.is_residential = is_residential
    def calculate_postage_cost(self):
        if self.is_residential:
            return 4
        else:
            return 10
    def __str__(self):
        postage_cost = self.calculate_postage_cost()
        return f"Shipping to {self.street}, {self.city}({self.postal_code}) costs ${postage_cost}."
class Person:
    def __init__(self, name, street, city, postal_code, is_residential):
        self.address = Address(street, city, postal_code, is_residential)
        self.name = name
    def __str__(self):
        return "{}: {}.".format(self.name, self.address)

person1 = Person("Dick Smith", "34 Princess Street", "Auckland", 1010, False)
person2 = Person("Michael Hill", "1023 Westmoreland Street", "Auckland", 1021, True)
print(person1)
print(person2)
print(type(person1))
print(type(person1.address))




