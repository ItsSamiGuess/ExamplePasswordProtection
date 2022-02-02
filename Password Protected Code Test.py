#Password Protected Code(ish)
from time import sleep
import datetime
import sys
import calendar

print("Log Into Your Account")
print("If you wish to log in with GitHub or Google, please choose accordingly.")
print("")

Tries = 6
while True:
    if Tries == 0:
        print("")
        sleep(2)
        print("you have too many failed attempts. Stutting down...")
        sleep(5)
        sys.exit()    
    while Tries > 0:    
        userName = input("Please Enter Your Username or Email or Phone Number: ")
        if userName == ('john'):
            while True:
                Pass= input("Please Enter Your Password: ")
                if Pass ==("123"):
                    print("Login Succesful.")
                    sleep(2)
                    while True:
                        loginDate = input("Do you wish to stay logged in for 30 days? (y/n): ")
                        if loginDate == ("y"):
                            current_time = datetime.datetime.now() 
                            print ("The Current Time and Date is (In terms of first login):", current_time.year, current_time.month, current_time.day)
                            InitiationDate = current_time.month + 1  
                else: 
                    Tries -= 1
                    print("Password Incorrect. You have ", Tries, "Attempt(s) Left.")
                    sleep(2)
                    print("( Remember that the system is extremely sensitive to CAPITALIZATION and S p a c i n g. )")
                    print("")
                    sleep(2)
                    continue
        else:
            Tries -= 1
            print("Username or Password is incorrect. You have", Tries, "Attempt(s) Left.")
            sleep(2)
            print("")
            print("( Remember that the system is extremely sensitive to CAPITALIZATION and S p a c i n g. )")
            continue   


