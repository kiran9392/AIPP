class Student:
    def __init__(self, name, roll_no):  # ✅ Added 'self'
        self.name = name
        self.roll_no = roll_no

    def display_details(self):  # ✅ Added 'self'
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

# Creating object and displaying details
s1 = Student("Shiva", 121)
s1.display_details()
