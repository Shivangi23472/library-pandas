import pandas as pd
def view_book():
    data=pd.read_csv("book.csv",sep=",")
    print(data)

