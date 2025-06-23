class Candidate:
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

class Student(Candidate):
    def __init__(self, name, id_no, branch):
        super().__init__(name, id_no) 
        self.branch = branch

class Faculty(Candidate):
    def __init__(self, name, id_no, branch, subject):
        super().__init__(name, id_no)
        self.dept = branch
        self.subject = subject

class College:
    def __init__(self, name):
        self.clg_name = name
        self.students = []
        self.faculty_list = []

    def add_student(self, student):
        self.students.append(student)
        print("Student details have been updated successfully.")

    def add_faculty(self, faculty):
        self.faculty_list.append(faculty)
        print("Faculty details have been updated successfully.")

    def student_drop(self, student):
        self.students.remove(student)
        print("Student removed successfully.")

    def remove_faculty(self, faculty):
        self.faculty_list.remove(faculty)
        print("Faculty removed successfully.")

    def student_details(self):
        if not self.students:
            print("No students enrolled.")
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Enrollment Number: {student.id_no}")
            print(f"Branch: {student.branch}")
            print()

    def faculty_details(self):
        if not self.faculty_list:
            print("No faculty enrolled.")
        for faculty in self.faculty_list:
            print(f"Name: {faculty.name}")
            print(f"Employee Id: {faculty.id_no}")
            print(f"Department: {faculty.dept}")
            print(f"Subject: {faculty.subject}")
            print()

colleges = []

print("Choose an option")
print("1. New College Registration")
print("2. Student Enrollment")
print("3. Faculty Enrollment")
print("4. Student Drop")
print("5. Faculty Drop")
print("6. Student Details")
print("7. Faculty Details")
print("8. Exit")

while True:
    try:
        choice = int(input("Enter option number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        new_clg = input("Enter the name of the college you want to register: ")
        if any(college.clg_name == new_clg for college in colleges):
            print("College is already registered.")
        else:
            colleges.append(College(new_clg))
            print("College has been registered.")

    elif choice == 2:
        new_clg = input("Enter the name of the college you want to add a student to: ")
        current_clg = next((college for college in colleges if college.clg_name == new_clg), None)

        if current_clg:
            name = input("Enter the name of the student: ")
            id_no = input("Enter the enrollment id of the student: ")
            branch = input("Enter the branch in which they are admitted: ")
            current_clg.add_student(Student(name, id_no, branch))
        else:
            print("College does not exist.")

    elif choice == 3:
        new_clg = input("Enter the name of the college you want to add a faculty to: ")
        current_clg = next((college for college in colleges if college.clg_name == new_clg), None)

        if current_clg:
            name = input("Enter the name of the faculty: ")
            id_no = input("Enter the employee id of the faculty: ")
            branch = input("Enter the department: ")
            sub = input("Enter the subject they teach: ")
            current_clg.add_faculty(Faculty(name, id_no, branch, sub))
        else:
            print("College does not exist.")

    elif choice == 4:
        new_clg = input("Enter the name of the college to drop a student from: ")
        current_clg = next((college for college in colleges if college.clg_name == new_clg), None)

        if current_clg:
            student_id = input("Enter enrollment number of the student: ")
            student = next((s for s in current_clg.students if s.id_no == student_id), None)
            if student:
                current_clg.student_drop(student)
            else:
                print("No student found with that enrollment number.")
        else:
            print("College does not exist.")

    elif choice == 5:
        new_clg = input("Enter the name of the college to drop a faculty from: ")
        current_clg = next((college for college in colleges if college.clg_name == new_clg), None)

        if current_clg:
            faculty_id = input("Enter employee id of the faculty: ")
            faculty = next((f for f in current_clg.faculty_list if f.id_no == faculty_id), None)
            if faculty:
                current_clg.remove_faculty(faculty)
            else:
                print("No faculty found with that employee id.")
        else:
            print("College does not exist.")

    elif choice == 6:
        new_clg = input("Enter the name of the college: ")
        current_clg = next((college for college in colleges if college.clg_name == new_clg), None)

        if current_clg:
            current_clg.student_details()
        else:
            print("College does not exist.")

    elif choice == 7:
        new_clg = input("Enter the name of the college: ")
        current_clg = next((college for college in colleges if college.clg_name == new_clg), None)

        if current_clg:
            current_clg.faculty_details()
        else:
            print("College does not exist.")

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid input. Try another option.")
