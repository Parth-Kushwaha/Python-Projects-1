# Student Management System
# MAIN MODULE
"""
Fields :- ['ENROLLMENT', 'NAME', 'AGE', 'EMAIL', 'PHONE']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Marks Menu
7. Teacher's Menu
9. QUIT
"""
import MARKS
import TEACHER
import csv
# Define global variables
student_fields = ['ENENROLLMENTMENT NO: ', 'NAME:', 'AGE', 'EMAIL:', 'PHONE:']
student_database = 'students.csv'


def password():
    passw="admin"
    x=input("ENTER THE PASSWORD TO LOGIN:  ")
    if passw==x:
        
        def display_menu():
            print("--------------------------------------")
            print("*** Welcome to Student Management System")
            print("---------------------------------------")
            print("*** 1. ADD NEW STUDENT")
            print("*** 2. VIEW STUDENTS")
            print("*** 3. SEARCH STUDENT")
            print("*** 4. UPDATE STUDENT")
            print("*** 5. DELETE STUDENT")
            print("*** 6. MARKS OF STUDENT MENU")
            print("*** 7. TEACHER DETAILS MENU")
            print("*** 8. TO EXIT THE SYSTEM")


        def add_student():
            print("-------------------------")
            print("ADD STUDENT INFORMATION")
            print("-------------------------")
            global student_fields
            global student_database

            student_data = []
            for field in student_fields:
                value = input("ENTER " + field + ": ")
                student_data.append(value)

            with open(student_database, "a", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows([student_data])

            print("DATA SAVED SUCCESSFULLY")
            input("PRESS ANY KEY TO CONTINUE")
            return


        def view_students():
            global student_fields
            global student_database

            print("--- STUDENT RECORDS ---")

            with open(student_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for x in student_fields:
                    print(x, end='\t |')
                print("\n-----------------------------------------------------------------")

                for row in reader:
                    for item in row:
                        print(item, end="\t |")
                    print("\n")

            input("PRESS ANY KEY TO CONTINUE")


        def search_student():
            global student_fields
            global student_database

            print("--- SEARCH STUDENT---")
            ENROLLMENT = input("ENTER ENROLLMENT NO. TO SEARCH: ")
            with open(student_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) > 0:
                        if ENROLLMENT == row[0]:
                            print("----- Student Found -----")
                            print("ENROLLMENT: ", row[0])
                            print("NAME: ", row[1])
                            print("AGE: ", row[2])
                            print("EMAIL: ", row[3])
                            print("PHONE: ", row[4])
                            break
                else:
                    print("ENROLLMENT NO. NOT FOUND IN THE DATABASE")
            input("PRESS ANY KEY TO CONTINUE")


        def update_student():
            global student_fields
            global student_database

            print("--- Update Student ---")
            ENROLLMENT = input("ENTER ENROLLMENT NO. TO UPDATE: ")
            index_student = None
            updated_data = []
            with open(student_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                counter = 0
                for row in reader:
                    if len(row) > 0:
                        if ENROLLMENT == row[0]:
                            index_student = counter
                            print("SSTUDET FOUND AT INDEX: ",index_student)
                            student_data = []
                            for field in student_fields:
                                value = input("ENTER " + field + ": ")
                                student_data.append(value)
                            updated_data.append(student_data)
                        else:
                            updated_data.append(row)
                        counter += 1


            # Check if the record is found or not
            if index_student is not None:
                with open(student_database, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_data)
            else:
                print("ENROLLMENT NO. NOT FOUND IN OUR DATABASE")

            input("PRESS ANY KEY TO CONTINUE")


        def delete_student():
            global student_fields
            global student_database

            print("--- Delete Student ---")
            ENROLLMENT = input("ENTERENROLLMENT NO. TO DELETE: ")
            student_found = False
            updated_data = []
            with open(student_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                counter = 0
                for row in reader:
                    if len(row) > 0:
                        if ENROLLMENT != row[0]:
                            updated_data.append(row)
                            counter += 1
                        else:
                            student_found = True

            if student_found is True:
                with open(student_database, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_data)
                print("ENROLLMENT NO. ", ENROLLMENT, "DELETED SUCCESSFULLY")
            else:
                print("ENROLLMENT NO. NOT FOUND IN OUR DATABASE")

            input("PRESS ANY KEY TO CONTINUE")

        while True:
            display_menu()

            choice = input("ENTER YOUR CHOICE: ")
            if choice == '1':
                add_student()
            elif choice == '2':
                view_students()
            elif choice == '3':
                search_student()
            elif choice == '4':
                update_student()
            elif choice == '5':
                delete_student()
            elif choice =='6':
                MARKS.menu()
            elif choice=='7':
                TEACHER.menu()
            elif choice=='8':
                break
            else:
                print(" PLEASE ENTER CHOOSE A CORRECT OPTION")
                

        print("-------------------------------")
        print(" THANK YOU FOR USING OUR PROGRAM")
        print("-------------------------------")

    else:
        print("INVALID PASSWORD ENTERED")
        print("PLEASE ENTER AGAIN")
        password()
password()












        
