import pandas as pd
from datetime import date,timedelta,datetime
from addbook import add_book
from captcha import captcha
from finebook import fine_book
from issue import issue_book
from returnbook import return_book
from viewbook import view_book
while True:
    print("\t\t\t\t\t\t WELCOME TO THE CENTRAL LIBRARY PORTAL\t\t\t\t\t\t\t")
    print("press 1 to view books")
    print("press 2 to add books")
    print("press 3 to issue book")
    print("press 4 to return book")
    print("press 5 to exit")
    choice=input("Select a choice: ")

    if choice=="1":
        view_book()
        
    elif choice=="2":
        add_book()
        
    elif choice=="3":
        issue_book()
        
    elif choice=="4":
        return_book()
        
    elif choice=="5":
        exit()
    else:
        print("Please select a valid choice")
    