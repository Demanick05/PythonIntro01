"""
Create class "Group", which stores a list of objects "student", created from the corresponding class "Student".
Implement a decent set of methods and attributes to work with these objects.
"""


# Creating a "Student" class


class Student:
    def _init_(self, age, name, gender, *grades):
        self.age = age
        self.grades = [grades]
        self.name = str(name)
        self.gender = str(gender)

    def add_grade(self, *new_grade):
        grades = []
        grades.append(new_grade)
        return grades

    def avg_grade(self):
        avg_value = sum(self.grades) // len(self.grades)
        return avg_value


# Creating a "Group" class
class Group(Student):
    def init(self, stud_list):
        self.stud_list = stud_list
        return stud_list

    def group(self, *students):
        stud_list = []
        stud_list.append(students)
        return stud_list


ivan = Student()
ivan.name = "Ivan"
ivan.grades = [5, 2, 5, 4, 2, 3]
ivan.gender = "Male"
ivan.age = 20

maria = Student()
maria.gender = "Female"
maria.name = "Maria"
maria.age = "22"
maria.grades = [3, 4, 1, 5, 2]

group = Group()
group.group(ivan, maria)
