#MARKS OF ALL SUBJECTS
'''
-------------------------------------
FUNCTIONS PERFORMED BY THIS MODULE-
-------------------------------------
1. ENTERING THE MARKS OF EACH STUDENT.
2. VIEW THE ENTERED MARKS.
3. UPDATE THE ENTERED MARKS.
4. SEARCH FOR A RECORD
5. DELETE A RECORD
6. TO SEARCH FOR RECORD BY MARKS GREATER OR LOWER(SEPARATE FUNCTIONS)
'''

import pickle
import os

def enter():                                                              #ENTER STUDENT DETAILS 
    fout=open("marks.dat","ab")
    ch='y'                                                                 #opening in append so that previous file does not gets deleted
    
    print("KINDLY ENTER STUDENT'S MARKS-")
    try:
        while ch=='y'or ch=='Y':
            enroll=(input("ENROLLMENT NUMBER: "))                        #input enrollment
            a=int(input("ENTER CS MARKS:"))                                       #input marks 
            b=int(input("MATHS:"))
            c=int(input("CHEMISTRY:"))
            d=int(input("PHYSICS:"))
            e=int(input("ENGLISH: "))
            f= (a+b+c+d+e)/500
            p=f*100

            stu={ }                                                            #creating a dictionary to store values
            stu["ENROLLMENT"]= enroll
            stu["CS"]= a
            stu["MATHS"]= b
            stu["CHEMISTRY"]= c
            stu["PHYSICS"]= d
            stu["ENGLISH"]= e
            stu["PERCENTAGE"]= p

            pickle.dump(stu,fout)                                            #dumping into the file
            print("RECORD SAVED IN FILE!")
            print(stu)
            ch=input("DO YOU WANT TO ENTER MORE STUDENT MARKS? (Y/N): ")
        fout.close()
    except ValueError:
        print("*"*35)
        print("--> YOU HAVE ENTERED A WRONG VALUE")
        print()
        
        print("--> PLEASE ENTER A INTEGER VALUE")
        print("*"*35)                                                                                                         
    
def view():                                                    # VIEW THE MARKS 
    fin=open("marks.dat","rb")

    try:
        while True:
            obj=pickle.load(fin)
            print(obj)
            print()
    except EOFError:
        fin.close()
        print("File Complete")


def update():                                                                 # to update a record
    fin=open("marks.dat","rb")                                             #read from this file
    fout=open("temp.dat","ab")                                           # write in this file

    found=False

    enroll=(input("ENROLLMENT NO TO UPDATE: "))

    try:
        while True:
            obj=pickle.load(fin)                                                       # loading the data from fin
            if obj["ENROLLMENT"]==enroll:                       #if the enroll entered matches with one of the records
                found=True
                print(obj)
                print("RECORD FOUND ENTER NEW DETAILS: ")
                enroll=(input("ENTER NEW ENROLLMENT NO. : "))
                a=int(input("ENTER CS MARKS:"))                                       #input new marks 
                b=int(input("MATHS:"))
                c=int(input("CHEMISTRY:"))
                d=int(input("PHYSICS:"))
                e=int(input("ENGLISH: "))
                f= a+b+c+d+e//500
                p=f*100
  
                stu={ }                                                  # storing in dictionary
                stu["ENROLLMENT "]= enroll
                stu["CS"]= a
                stu["MATHS"]= b
                stu["CHEMISTRY"]= c
                stu["PHYSICS"]= d
                stu["ENGLISH"]= e
                stu["PERCENTAGE"]= p

                pickle.dump(stu,fout)                           # wrting new record in fout
                print("RECORD UPDATED")
            

            
            else:
                pickle.dump(obj,fout)                     # if the enroll dosent match then write the record without any changes

    except EOFError:
        fin.close()                                              #closing both the files
        fout.close()
    except ValueError:
        print("*"*30)
        print("--> PLEASE ENTER A INTEGER VALUE!")
        print("*"*30)
    except PermissionError:
        print("*"*30)
        print("--> WRONG VALUE ENTERED")
        print("*"*30)

        os.remove("marks.dat")                              # deleting the previous file
        os.rename("temp.dat","marks.dat")   # renaming the new file with the previous one's name

    if found==False:                                                       # if the entered eroll does not match any record
        print("NO RECORD FOUND WITH THIS ENROLLMENT NUMBER!!")

    print("NOW FILE CONTAINS.....")

    fin=open("marks.dat","rb")                      # reading the file to ensure the user 

    try:
        while True:
            obj=pickle.load(fin)
            print(obj)
            print()
    except EOFError:
        fin.close()
        print("FILE COMPLETE")

def search():
    fin=open("marks.dat","rb")
    ch='y'
    roll=input("ENTER THE ENROLLMENT YOU WANT TO SEARCH: ")
    try:
        while ch=='y' or ch=='Y':
            obj=pickle.load(fin)
            if obj["ENROLLMENT"]== roll:
                print("RECORD FOUND:")
                print(obj)
               
        else:
            print("NO SUCH RECORD FOUND")
    except:
        fin.close()

def delete():
    fin=open("marks.dat","rb")
    fout=open("tempe.dat","ab")
    found= False
    ch='y'
    roll=input("ENTER THE ENROLLMENT NUMBER OF THE STUDENT")
    try:
        while ch=='y' or ch=='Y':
            obj=pickle.load(fin)
            if obj["ENROLLMENT"]== roll:
                   found=True
                   print("RECORD DELETED")
            else:
                   pickle.dump(obj,fout)
    except:
        fin.close()
        fout.close()
    os.remove("marks.dat")
    os.rename("tempe.dat","marks.dat")
    if found== False:
        print("RECORD NOT FOUND")

def greater():
    fin=open("marks.dat","rb")
    ch='y'
    try:
        x=int(input("ENTER THE MARKS YOU WANT RECORDS GREATER THAN: "))
        print("RECORDS GREATER THAN",x,"ARE:" )
        while ch=='y' or ch=='Y':
            obj=pickle.load(fin)
            if obj["PERCENTAGE"]> x:
                print(obj)
                print()
        else:
            print("NO STUDENT HAS A TOTAL SCORE ABOVE",x)
    except EOFError:
        fin.close()
    except ValueError:

        print("*"*30)
        print("PLEASE ENTER A INTEGER VALUE B/W 1-100")
        print("*"*30)
def lower():
    fin=open("marks.dat","rb")
    ch='y'
    try:
        x=int(input("ENTER THE MARKS YOU WANT RECORDS LOWER THAN: "))
        if x<0 or x>100:
            print("PLEASE ENTER A INTEGER VALUE B/W 1=100")
        else:
            while ch=='y' or ch=='Y':
                obj=pickle.load(fin)
                if obj["PERCENTAGE"]<x:
                    print(obj)
                    print()
            else:
                print("NO STUDENT HAS SCORED LOWER THAN",x)
    except EOFError:
        fin.close()
    except ValueError:
       print("*"*30)
       print("PLEASE ENTER AN INTEGER VALUE")
       print("*"*30)        

def menu():                                                          #menu of the file
    ch='y'
    print("-"*45)
    print("|| ||  WELCOME TO STUDENT MARKS MENU!   || ||")
    print("-"*45)
    while True:
        print("|| ||  1. TO ENTER STUDENT'S MARKS")
        print("|| ||  2. TO VIEW THE MARKS")
        print("|| ||  3. TO UPDATE A EXISTING RECORD OF MARKS")
        print("|| ||  4. TO SEARCH FOR A RECORD")
        print("|| ||  5. TO DELETE A RECORD")
        print("|| ||  6. TO SHOW THE RECORDS GREATER BY")
        print("|| ||  7. TO SHOW THE RECORDS LOWER THAN")
        print("|| ||  8. TO EXIT THE PROGRAM")
        ch=(input("ENTER YOUR CHOICE: "))

        if ch=="1":
            enter()
        elif ch=="2":
            view()
        elif ch=="3":
            update()
        elif ch=="4":
            search()
        elif ch=="5":
            delete()
        elif ch=="6":
            greater()
        elif ch=="7":
            lower()
        elif ch=="8":
            print("THANK YOU FOR USING THE PROGRAM, YOU ARE NOW EXITING THE PROGRAM")
            break
        else:
            print("PLEASE ENTER CORRECT VALUE!")
            
#menu()







        



