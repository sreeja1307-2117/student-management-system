
"""
Student Management System

Features:
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student
- JSON Storage
- Input Validation

Created using Python
"""

import json
#save student data in json file
def save_data(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []#list where whole data stored


def add_student():
        
    while True:
        student = {}
        student["name"] = input("Enter student name: ")
        while True:
          
          try:
              
            student["age"] = int(input("Enter student age: "))
            if student["age"] < 0:
                print("Enter valid age")
                continue
            break
          
          except ValueError:
            print("Enter valid age")
            
        while True:  
          try:
            student["marks"] = int(input("Enter student marks: "))
            if student["marks"] < 0 or student["marks"] > 100:
                print("Enter valid marks (0-100)")        
                continue
            break
          except ValueError:
            print("Enter valid marks") 
            
            
        students.append(student)
        save_data(students)
        another = input("Do you want to add another student? (yes/no): ")
        if another.lower() == "no":
           break


def view_students():
        print("view student feature")
        if len(students)==0:
            print("No students found")
        else:
            print("\n===== STUDENT LIST =====")

            for student in students:
                print("Name:",student["name"])
                print("Age:",student.get("age","N/A"))
                print("Marks:",student.get("marks","N/A"))

                print("\n========================")


def search_student():
        search_name = input("Enter student name to search: ").strip()
        found = False
        for student in students:
            if student["name"].lower()== search_name.lower():
                print("\n Student found:")
                print("Name", student["name"])
                print("Age", student.get("age","N/A"))
                print("Marks", student.get("marks","N/A"))

                found = True
                break
        if not found:
            print("Student not found.")


def delete_student():
        
        delete_name = input("Enter student name to delete:").strip()
        found = False
        for student in students:
            if student["name"].lower()== delete_name.lower().strip():
                students.remove(student)
                save_data(students)
                print("Student removed successfully")
                found = True
                break
        if not found:
            print("student not found")


def update_student():
    student_name = input("Enter student name to update: ").strip()
    found = False
    for student in students:
        if student["name"].lower() == student_name.lower():
            found = True
            while True:
                print("What do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Marks")
                choice = input("Enter your choice: ").strip()
                
                if choice == "1":
                    new_name = input("Enter new name: ")
                    student["name"] = new_name
                    save_data(students)
                    print("Name updated successfully")
                    break


                elif choice == "2":
                    try:
                        new_age = int(input("Enter new age: "))
                        student["age"] = new_age
                        save_data(students)
                        print("Age updated successfully")
                        break
                    except ValueError:
                        print("Enter valid age")
                
    
                elif choice == "3":
                    try:
                        new_marks = int(input("Enter new marks: "))
                        student["marks"] = new_marks
                        save_data(students)
                        print("Marks updated successfully")
                        break
                    except ValueError:
                        print("Enter valid marks")
                else:
                    print("Invalid choice. Please try again.")
            break
    if not found:
        print("Student not found")

def exit_system():
    print("Thank you for visiting. goodbye")

if __name__ == "__main__":
   while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            exit_system()
            break
        else:
            print("Invalid choice. Please try again.")