from datetime import date, datetime
class ATM:
    def __init__(self):
        self.amount=50000
        self.pin=1234
        self.ms=[]
    def withdraw(self,s):
        p=int(input("enter pin :"))
        if(self.pin==p):
            if(self.amount>s):
                self.amount=self.amount-s
                x=datetime.now()
                str1=f'{x} : -{s}'
                self.ms.append(str1)
                print("Remaining balance: {}            Transaction time: {}".format(self.amount,x))
            else:
                print("not sufficient")
        else:
            print("incorrect pin")
    def deposit(self,d):
        p=int(input("enter pin :"))
        if(self.pin==p):
            self.amount+=d
            x=datetime.now()
            str1=f'{x} : +{d}'
            self.ms.append(str1)
            print("Updated balance: {}            Transaction time: {}".format(self.amount,x))
        else:
            print("incorrect pin")
    def change(self):
        x=datetime.now()
        p=int(input("enter pin :"))
        if(p==self.pin):
            k=int(input("enter new pin :"))
            k1=int(input("enter new pin once again :"))
            if(k==k1):
                self.pin=k
                print("pin changed successfully!!!        Transaction time: {}".format(x))
                j=f'{x}:updated'
                self.ms.append(j)
            else:
                print("Try again")
        else:
            print("Incorrect pin Try again")
    def ministatement(self):
        p=int(input("enter pin :"))
        if(self.pin==p):
            if(len(self.ms)==0):
                print("no transaction")
            else:
                print("|-------------------------------------------------------|")
                for i in self.ms[-5:]:
                    
                    print('|          ',i,'         |')
                print("|-------------------------------------------------------|")
                print("Balence money :",self.amount)   
a=ATM()
for _ in range(100):
    c=int(input("1)withdraw\n2)deposit\n3)change\n4)ministatement\n5)exit\nEnter an option from 1 to 5:"))
    if(c==1):
        s=int(input("Enter the amount to withdraw: "))
        a.withdraw(s)
    if(c==2):
        d=int(input("Enter the amount to deposit: "))
        a.deposit(d)
    if(c==3):
        a.change()
    if(c==4):
        a.ministatement()
    if(c==5):
        exit(0)
    if(c>5 or c<1):
        print("Enter valid number")
