class Student:
    # Static list to hold all student records
    students = []

    def __init__(self, student_id, name, age, email, course):
        # Initialize the student's attributes
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course

    @staticmethod
    def save_student(student):
        # Add the student to the students list
        Student.students.append(student)
        print("Student details have been successfully saved.")

    @staticmethod
    def search_student(student_id):
        # Iterate through the list to find the student with the given ID
        for student in Student.students:
            if student.student_id == student_id:
                return student
        return None

    @staticmethod
    def delete_student(student_id):
        # Search for the student in the list
        student = Student.search_student(student_id)
        if student:
            Student.students.remove(student)  # Remove the student if found
            return True
        return False

    @staticmethod
    def student_report():
        # Print a report of all students
        count = 1
        for student in Student.students:
            print(f"\nSTUDENT {count}")
            print("------------------------------")
            print(f"STUDENT ID: {student.student_id}")
            print(f"STUDENT NAME: {student.name}")
            print(f"STUDENT AGE: {student.age}")
            print(f"STUDENT EMAIL: {student.email}")
            print(f"STUDENT COURSE: {student.course}")
            print("------------------------------")
            count += 1

    @staticmethod
    def exit_student_application():
        # Farewell message and exit
        print("Exiting the application. Goodbye!")
        exit()

class StudentManagementApplication:
    @staticmethod
    def show_menu():
        # Display the main menu to the user
        print("\nPlease select one of the following menu items:")
        print("(1) Capture a new student.")
        print("(2) Search for a student.")
        print("(3) Delete a student.")
        print("(4) Print student report.")
        print("(5) Exit Application.\n")

    @staticmethod
    def capture_student():
        # Capture new student details
        print("\nCAPTURE A NEW STUDENT")
        print("*****************************")

        student_id = input("Enter the student id: ")
        name = input("Enter the student name: ")

        age = StudentManagementApplication.capture_student_age()

        email = input("Enter the student email: ")
        course = input("Enter the student course: ")

        student = Student(student_id, name, age, email, course)
        Student.save_student(student)

    @staticmethod
    def capture_student_age():
        # Validate the student's age to ensure it is a valid number and within the acceptable range
        while True:
            try:
                age = int(input("Enter the student age: "))
                if age < 16:
                    print("You have entered an incorrect student age!!! Please re-enter the student age >>")
                else:
                    return age
            except ValueError:
                print("You have entered an incorrect student age!!! Please re-enter the student age >>")

    @staticmethod
    def search_student():
        # Search for a student by their ID and display their details
        student_id = input("Enter the student id to search: ")

        student = Student.search_student(student_id)
        if student:
            print("\n---------------------------------------------")
            print(f"STUDENT ID: {student.student_id}")
            print(f"STUDENT NAME: {student.name}")
            print(f"STUDENT AGE: {student.age}")
            print(f"STUDENT EMAIL: {student.email}")
            print(f"STUDENT COURSE: {student.course}")
            print("---------------------------------------------")
        else:
            print("\n---------------------------------------------")
            print(f"Student with Student Id: {student_id} was not found!")
            print("---------------------------------------------")

    @staticmethod
    def delete_student():
        # Delete a student record after user confirmation
        student_id = input("Enter the student id to delete: ")
        confirmation = input(f"Are you sure you want to delete student {student_id} from the system? Yes (y) to delete: ")

        if confirmation.lower() == 'y':
            success = Student.delete_student(student_id)
            if success:
                print("\n---------------------------------------------")
                print(f"Student with Student Id: {student_id} WAS deleted!")
                print("---------------------------------------------")
            else:
                print("\n---------------------------------------------")
                print(f"Student with Student Id: {student_id} was not found!")
                print("---------------------------------------------")

    @staticmethod
    def main():
        # Main method to run the application
        print("STUDENT MANAGEMENT APPLICATION")
        print("*************************************************")
        initial_choice = input("Enter (1) to launch menu or any other key to exit: ")

        if initial_choice != "1":
            print("Exiting the application. Goodbye!")
            exit()

        while True:
            StudentManagementApplication.show_menu()
            choice = input()

            if choice == "1":
                StudentManagementApplication.capture_student()
            elif choice == "2":
                StudentManagementApplication.search_student()
            elif choice == "3":
                StudentManagementApplication.delete_student()
            elif choice == "4":
                Student.student_report()
            elif choice == "5":
                Student.exit_student_application()
            else:
                print("Invalid choice! Please enter a valid menu option.\n")


# Run the application
if __name__ == "__main__":
    StudentManagementApplication.main()
