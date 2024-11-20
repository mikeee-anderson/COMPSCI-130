class Student:
    def __init__(self, name="UNKNOWN", age=1, student_id=1):
        self.name = name
        self.age = age
        self.student_id = student_id
    def __str__(self):
        return f"{self.name}({self.age}),{self.student_id}"

student1 = Student()
print(student1, student1.name, student1.age, student1.student_id)
student2 = Student("Dick Smith", 56, 123456)
print(student2, student2.name, student2.age)
print(student1 == student2)
print(type(student1))