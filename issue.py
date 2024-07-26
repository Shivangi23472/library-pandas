import pandas as pd
from datetime import date,timedelta

def issue_book():
    roll=int(input("enter roll no"))
    data=pd.read_csv("student.csv",sep=",")
    book=pd.read_csv("book.csv",sep=",")
    fine=pd.read_csv("fine.csv",sep=",")
    if roll in list(data["roll"]):
        b=input("enter book name: ")
        if b in list(book["book"]):
             val=fine[(fine["roll"]==roll) & (fine["book"]==b)&(pd.isna(fine["ar"]))]
             if len(val)==1:
                 print("You have already issued this book")
             else:
              ind=list(book["book"]).index(b)
              if(book["qty"][ind]>0):
                temp={"roll":[roll],"book":[b],"issue":[date.today()],"er":[date.today()+timedelta(days=7)]}
                temp2=pd.DataFrame(temp)
                fine=pd.concat([fine,temp2],axis=0)
                fine.to_csv("fine.csv",index=False)
                book["qty"][ind]=book["qty"][ind]-1
                book.to_csv("book.csv",index=False)
                print("book issued successfully")
              else:
                print("book out of stock")
        else:
            print("invalid bookname")
    else:
        print("invalid roll no")
