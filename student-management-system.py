class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def create_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = {'name': name, 'age': age, 'grade': grade}
            print("Student added successfully.")

    def read_student(self, student_id=None):
        if student_id:
            if student_id in self.students:
                print(f"Student ID: {student_id}, Details: {self.students[student_id]}")
            else:
                print("Student not found.")
        else:
            if self.students:
                for id, details in self.students.items():
                    print(f"Student ID: {id}, Details: {details}")
            else:
                print("No students found.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.students:
            if name:
                self.students[student_id]['name'] = name
            if age:
                self.students[student_id]['age'] = age
            if grade:
                self.students[student_id]['grade'] = grade
            print("Student updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")


# Main program
def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            sms.create_student(student_id, name, age, grade)

        elif choice == '2':
            student_id = input("Enter student ID to view: ")
            sms.read_student(student_id)

        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            sms.update_student(student_id, name or None, age or None, grade or None)

        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            sms.delete_student(student_id)

        elif choice == '5':
            sms.read_student()

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
