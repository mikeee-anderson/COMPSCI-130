class Course:
    def __init__(self, name="UNKNOWN", number_of_students=0):
        self.name = name
        self.number_of_students = number_of_students

    def __str__(self):
        return f"{self.name}({self.number_of_students})"

    def register(self):
        self.number_of_students += 1

    def un_register(self):
        if self.number_of_students > 0:
            self.number_of_students -= 1

class Student:
    def __init__(self, name, username, max_count=1):
        self.name = name
        self.username = username
        self.max_count = max_count
        self.courses = []
    def enrol(self, course):
        if len(self.courses) < self.max_count:
            self.courses.append(course)
            course.register()
    def un_enrol(self, course):
        if len(self.courses) != 0 and isinstance(course, Course) and course in self.courses:
            self.courses.remove(course)
            course.un_register()
    def __str__(self):
        if len(self.courses) == 0:
            return f"{self.name}: Not enrolled in any courses."
        else:
            courses_str = ", ".join(str(course) for course in self.courses)
            return f"{self.name} enrolled: [{courses_str}] course(s)."
