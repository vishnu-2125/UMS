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

    def add_student(self,student):
        self.students.append(student)
        print("student details have been updated successfully ")

    def add_faculty(self, faculty):
        self.faculty_list.append(faculty)
        print("Faculty details have been updated successfully ")

    def student_drop(self, student):
        self.students.remove(student)
        print("student details have been updated successfully ")

    def remove_faculty(self, faculty):
        self.faculty_list.remove(faculty)
        print("Faculty details have been updated successfully ")

    def student_details(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Enrollement Number: {student.id_no}")
            print()

    def faculty_details(self):
        for faculty in self.faculty_list:
            print(f"Name: {faculty.name}")
            print(f"Employee Id: {faculty.id_no}")
            print()
colleges = []
print("Choose an option")
print("1.New College Registration")
print("2. Student Enrollment")
print("3. Factuly Enrollment")
print("4. Student Drop")
print("5. Faculty Drop")
print("6. Student Details")
print("7. Faculty Details")
print("8. Exit")

while True:
    choice = int(input("Enter option number"))

    if choice == 1:
        new_clg = input("Enter the name of the college you want to register: ")
        exist = False
        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                break

        if exist:
            print("College is already registered")
        else:
            clg_obj = College(new_clg)
            colleges.append(clg_obj)
            print("College has been registered.")

    elif choice == 2:
        new_clg = input("Enter the name of the college you want to add a student: ")
        exist = False

        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                current_clg = college
                break

        if exist:
            name = input("Enter the name of the student: ")
            id_no = input("Enter the enrollment id of student: ")
            branch = input("Enter the branch in which they are admitted: ")
            new_student = Student(name, id_no, branch)
            current_clg.add_student(new_student)
            print("Student details updated")
                      
        else:
            print("college does not exist.")

    elif choice == 3:
        new_clg = input("Enter the name of the college you want to add a faculty: ")
        exist = False

        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                current_clg = college
                break

        if exist:
            name = input("Enter the name of the faculty: ")
            id_no = input("Enter the enrollment id of faculty: ")
            branch = input("Enter the branch in which they are: ")
            sub = input("Enter the subject they teach: ")
            new_faculty =  Faculty(name, id_no, branch, sub)
            current_clg.add_faculty(new_faculty)
            print("Faculty details updated")
                      
        else:
            print("college does not exist.")
            
    elif choice == 4:
        new_clg = input("Enter the name of the college you want to drop a student: ")
        exist = False

        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                current_clg = college
                break

        if exist:
            
            student_id = input("Enter enrollment number of student: ")
            student_exist = False
            for student in current_clg.students:
                if student.id_no == student_id:
                    student_exist = True
                    current_student = student
            if student_exist:
                current_clg.student_drop(current_student)
                print("Student removed successfully.")
            else:
                print("No student with that details.")
                
        else:
            print("College does not exist")
    elif choice == 5:
        new_clg = input("Enter the name of the college you want to drop a student: ")
        exist = False

        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                current_clg = college
                break

        if exist:
            
            faculty_id = input("Enter enrollment number of student: ")
            faculty_exist = False
            for student in current_clg.faculty:
                if faculty.id_no == faculty_id:
                    faculty_exist = True
                    current_faculty = faculty
            if faculty_exist:
                current_clg.remove_faculty(current_faculty)
                print("faculty removed successfully.")
            else:
                print("No faculty with that details.")
                
        else:
            print("College does not exist")

    elif choice == 6:
        new_clg = input("Enter the name of the college: ")
        exist = False

        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                current_clg = college
                break

        if exist:
            current_clg.student_details()

        else:
            print("college does not exist")

    elif choice == 7:
        new_clg = input("Enter the name of the college: ")
        exist = False

        for college in colleges:
            if college.clg_name == new_clg:
                exist = True
                current_clg = college
                break

        if exist:
            current_clg.faculty_details()

        else:
            print("college does not exist")

    elif choice == 8:
        print("Thank you")
        break

    else:
        print("Invalid Input. Try some other.")
    