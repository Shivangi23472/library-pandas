import pandas as pd
from captcha import captcha
def add_book():
    user=input("Enter user name:")
    passwd=int(input("Enter password:"))
    status=captcha()
    data=pd.read_csv("book.csv",sep=",")
    if user=="admin" and passwd==1234 and status==1:
       book = input("Enter book name:")
       booklist=list(data["book"])
       if book  in booklist:
           ind = booklist.index(book)
           num=int(input("Enter quantity"))
           data["qty"][ind]=data["qty"][ind]+num
           data.to_csv("book.csv",index=False)
           print("New book has been added succssfully")
       else:
           num=int(input("Enter quantity: "))
           price=int(input("Enter price in rupees: "))
           temp={"book":[book],"price":[price],"qty":[num]}
           temp2=pd.DataFrame(temp)
           data=pd.concat([data,temp2],axis=0)
           data.to_csv("book.csv",index=False)
           print("New book has been added succssfully")
    else:
        print("wrong credentials")
        add_book()

        



   
