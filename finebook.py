import pandas as pd
from datetime import date,timedelta,datetime
def fine_book(a):
  fine=pd.read_csv("fine.csv",sep=",")
  book=pd.read_csv("book.csv",sep=",")
  b=fine["er"][a]
  c=fine["ar"][a]
  date1=datetime.strptime(b,"%Y-%m-%d")
  date2=datetime.strptime(c,"%Y-%m-%d")
  
  dif=date2-date1
  if dif.days>0:
    charge=float(dif.days*10)
    print("you have been imposed fine of rupees ",charge)
    fine["charge"][a]=charge
    fine.to_csv("fine.csv",index=False)
   
  else:
    fine["charge"][a]=0.0
    fine.to_csv("fine.csv",index=False)
    print("book returned successfully")

 

  



'''  
a=date.today()
b=date(2024,7,28)
#b=a-timedelta(days=7)
print(a)
print(b)
f=b-a

if f.days>0 :
  print(f.days)
  print(f *10)
else:
  print("not ok")
'''

  
    