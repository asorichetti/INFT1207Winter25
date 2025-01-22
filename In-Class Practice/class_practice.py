class Student:
    def __init__(self, name='No Name', age='Ageless', student_id='Off the Grid'):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

student1 = Student("Alice", 20, 100998999)
student2 = Student("Alex", 22, 101000609)
student3 = Student()
student2.display_info()
student3.display_info()