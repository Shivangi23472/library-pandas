import pandas as pd
from datetime import date
from finebook import fine_book

def return_book():
   a=int(input("enter your roll number"))
   fine=pd.read_csv("E:/New folder/fine.csv",sep=",")
   
   data=pd.read_csv("student.csv",sep=",")
   book=pd.read_csv("book.csv",sep=",")
   if a in list(data["roll"]):
       b=input("enter bookname")
       if b in list(book["book"]):
         val=fine[(fine["roll"]==a) & (fine["book"]==b)&(pd.isna(fine["ar"]))]
         if len(val)==1:
          ind=fine.index.get_loc(val.index[0])
          print(ind)
          fine["ar"][ind]=date.today()
          fine.to_csv("E:/New folder/fine.csv",index=False)

          
          c=list(book["book"]).index(b)
          book["qty"][c]=book["qty"][c]+1
          book.to_csv("book.csv",index=False)
          fine_book(ind)
          #print("book returned successfully")
         
         else:
           print("you have not taken this book")
       else:
        print("invalid bookname")
   else:
      print("invalid rollno")


'''
fine=pd.read_csv("fine.csv",sep=",")
print(fine)
b="python"
ind=list(fine["book"]).index(b)
print(ind)
fine=fine.drop(ind,axis=0).reset_index(drop=True)
print(fine)
'''

