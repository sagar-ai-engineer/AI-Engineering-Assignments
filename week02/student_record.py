class Student:
    def __init__(self, name:str, grade, department):
        self.name = name
        self.grade = grade
        self.department = department
    
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Department: {self.department}")
    
    def update_grade(self, total_marks):
        if total_marks >= 33 and total_marks <= 100:
            if self.grade<12:
                self.grade+=1
                print("Promoted")
                self.print_info()
            else:
                print("Passed out")
        elif total_marks<33:
            print("Failed. Continue with same class")
            self.print_info()
        elif total_marks > 100:
            print("Invalid marks. Reevaluate!")


david = Student("David", 10, "AI and DS")
david.print_info()
david.update_grade(100)

sam = Student("Sam", 12, "AI and DS")
sam.print_info()
sam.update_grade(75)

dev = Student("Dev", 9, "Robotics")
dev.print_info()
dev.update_grade(30)



