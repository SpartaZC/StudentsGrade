class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_grades(self):
        print(f"\nStudent: {self.name}")
        print(f"Grades: {self.grades}")

        # lambda function inside OOP
        avg = lambda grades: sum(grades) / len(grades) if grades else 0

        average = avg(self.grades)
        print(f"Average: {average}")

        # lambda for pass/fail
        result = lambda x: "Pass" if x >= 50 else "Fail"
        print(f"Result: {result(average)}")


# Create student object
name = input("Enter student name: ")
student = Student(name)

# while loop menu
while True:
    print("\n--- MENU ---")
    print("1. Add grade")
    print("2. Show grades")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        grade = float(input("Enter grade: "))
        student.add_grade(grade)

    elif choice == "2":
        student.show_grades()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")