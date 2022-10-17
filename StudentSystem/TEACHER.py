#TEACHER DETAILS MODULE
'''
FUNCTIONS PERFORMED BY THE MODULE:
1. STORES TEACHER DEATILS
2. DISPLAYS THE DETAILS
3. CAN UPDATE THE DETAILS
4. CAN SEARCH FOR A PARTICULAR RECORD
5. CAN DELETE A PARTIULAR RECORD
'''

import pickle
import os

def enter_teacher():                                               # ENTERING THE TEACHER'S DETAILS.                                              
    fout=open("teacher.dat","ab")
    ch='y'
    try:
        while ch=='y' or ch=='Y':
            
            id1=input("ENTER THE TEACHER'S ID: ")
            name=input("ENTER TEACHER'S NAME: ")
            sub=input("ENTER THE NAME OF SUBJECT: ")
            cont=int(input("ENTER TEACHER'S CONTACT NUMBER: "))
            cont2=int(input("ENTER TEACHER'S SECOND CONTACT NO: "))

            teach={ }                                              #storing the values in a dictionary
            teach["IDENTITY"]= id1
            teach["NAME"]=name
            teach["SUBJECT"]= sub
            teach["CONTACT NUMBER 1"]=cont
            teach["CONTACT 2"]=cont2
            
            pickle.dump(teach,fout)                               #dumping the data into the file
            print("RECORD SAVED")
            ch=input("DO YOU WANT TO ENTER MORE RECORDS?(Y/N)")
        
    except ValueError:
        print("*"*30)
        print("YOU HAVE ENTERED WRONG VALUE")
        print("PLEASE ENTER THE CORRECT VALUE:")
        print("*"*30)
        fout.close()

def display_teacher():                                           # to display the teacher's record
    fin=open("teacher.dat","rb")
    try:
        print("-"*40)
        print("THE FILE CONTAINS THE FOLLOWING RECORDS:")
        print("-"*40)
        while True:
            obj=pickle.load(fin)                              #loading the records in a variable

            print(obj)
            print()
    except EOFError:                                       # when there are no more records in the file
        fin.close()


def update_teacher():                                    # to update a existing record in the file
    fin=open("teacher.dat","rb")                       # we will read from this file file
    fout=open("fake.dat","ab")                         # then we will dump the new record in this file along others
    found= False
    id2=input("ENTER THE IDENTITY OF TEACHER YOU WANT TO UPDATE: ")

    try:
        while True:
            obj=pickle.load(fin)                               # loading the records
            if obj["IDENTITY"]== id2:               
                found= True                                  # if the record is in the file
                print("RECORD FOUND")                # we enter new details
                id1=input("ENTER THE TEACHER'S ID: ")
                name=input("ENTER TEACHER'S NAME: ")
                sub=input("ENTER THE NAME OF SUBJECT: ")
                cont=int(input("ENTER TEACHER'S CONTACT NUMBER: "))
                cont2=int(input("ENTER TEACHER'S SECOND CONTACT NO: "))

                teach={ }
                teach["IDENTITY"]= id1
                teach["NAME"]=name
                teach["SUBJECT"]= sub
                teach["CONTACT NUMBER 1"]=cont
                teach["CONTACT NUMBER 2"]=cont2

                pickle.dump(teach,fout)
                print("RECORD UPDATED")
            else:
                pickle.dump(obj,fout)
    except ValueError:
        print("*"*30)
        print("--> Wrong Value Entered")
        print("*"*30)
        fin.close()
        fout.close()
    except PermissionError:
        print("*"*30)
        print("--> Wrong Value Entered")
        print("*"*30)
        os.remove("teacher.dat")                  # deleting the old file
        os.rename("fake.dat","teacher.dat")   # renaming the new file 
    
    if found==False:                             # if there is no such record
        print("RECORD NOT FOUND")        

def search_teacher():                        # to search for a record and display it
    fin=open("teacher.dat","rb")
    ch='y'
    id2= input("ENTER THE TEACHER'S IDENTITY: ")
    found= False
    try:
        while ch=='y' or ch=='Y':
            obj=pickle.load(fin)
            if obj["IDENTITY"]==id2:
                found= True
                print("RECORD FOUND")
                print(obj)
    except:
        fin.close()
    if found== False:
        print("RECORD NOT FOUND")

def delete_teacher():                             # to delete a existing record in the file
    fin=open("teacher.dat","rb")             # we read from this file
    fout=open("new.dat","ab")                  # we write in this file
    ch='y'
    id2= input("ENTER THE TEACHER'S IDENTITY YOU WANT TO DELETE: ")
    found= False
    try:
        while ch=='y' or ch=='Y':
            obj=pickle.load(fin)
            if obj["IDENTITY"]== id2:         # if record found we display the message
                found= True
                print("~"*20)
                print("BELOW RECORD DELETED")
                print(obj)
                print("~"*20)
            else:
                pickle.dump(obj,fout)    # we write all the records in fout except the one user wants to delete
    except:
        fin.close()
        fout.close()
    os.remove("teacher.dat")              # we delete the previous file
    os.rename("new.dat","teacher.dat") # and rename the file
    if found== False:                            # if there is no such reocord
        print("RECORD NOT FOUND")

def searchsub_teacher():                      # to search the teacher by their respective subjects
    fin=open("teacher.dat","rb")
    ch='y'
    sub=input("ENTER THE SUBJECT WHOSE TEACHERS YOU WANT TO DISPLAY:")
    found= False
    try:        
        while ch=='y' or ch=='Y':
            obj=pickle.load(fin)
            if obj["SUBJECT"].upper()== sub.upper():   # upper because if the user enters in lower case or mixed
                found= True
                print(obj)
    except:
        fin.close()
    if found== False:
        print("NO SUCH RECORD FOUND")

def menu():                                           # menu of the TEACHER'S module
    ch='y'
    while ch=='y' or ch=='Y':
        print("-"*40)
        print("|| WELCOME TO TEACHER'S MODULE")
        print("-"*40)
        print("|| 1. TO ENTER TEACHER'S DETAILS ")
        print("|| 2. TO DISPLAY TEACHER'S DETAILS")
        print("|| 3. TO UPDATE A TEACHER'S RECORD")
        print("|| 4. TO SEARCH FOR A TEACHER'S RECORD")
        print("|| 5. TO DELETE A TEACHER'S RECORD")
        print("|| 6. TO DISPLAY THE TEACHERS OF PARTICULAR SUBJECT")
        print("|| 7. TO EXIT THE MODULE ")
        ch1=input("ENTER YOUR CHOICE: ")

        if ch1=="1":
            enter_teacher()
        elif ch1=='2':
            display_teacher()
        elif ch1=='3':
            update_teacher()
        elif ch1=='4':
            search_teacher()
        elif ch1=='5':
            delete_teacher()
        elif ch1=='6':
            searchsub_teacher()
        elif ch1=='7':
            print("THANK YOU FOR USING THE PROGRAM")
            break
        else:
            print("PLEASE CHOOSE A OPTION AVAILABLE IN THE MENU")
            break


#menu()








    





            
        
            
