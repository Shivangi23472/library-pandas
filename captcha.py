import random
import string

def captcha():
    l=[]
    a="".join(random.choices(string.ascii_letters,k=3))
    a+="".join(random.choices(string.digits,k=2))
    
    b=list(a)
    random.shuffle(b)
    qr="".join(b)
    if qr not in l:
        l.append(qr)
        print("captcha: ",qr)
        user=input("Enter Captcha: ")
        if user==qr:
            return 1
    else:
        captcha()



    


