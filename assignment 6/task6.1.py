# Defining a Student class

class Student:
    def __init__(self, name, roll_no, grade):
        """
        Constructor to initialize the student's attributes.
        """
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display_details(self):
        """
        Method to display the student's details.
        """
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Grade: {self.grade}")


# Example usage
student1 = Student("Ramesh", 101, "A")
student1.display_details()
