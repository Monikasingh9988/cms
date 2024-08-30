"""
CUSTOMER MANAGEMENT SYSTEM USING BY OOPS:

"""
# BLL
class Customer:
    cus_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def Add_Customer(self):
        Customer.cus_list.append(self)
    def Search_Customer(self):
        for e in Customer.cus_list:
            if (e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                return
    def Delete_Customer(self):

        for e in Customer.cus_list:
            if (e.id==self.id):
                e.name=0
                e.age=0
                e.mob=0
                return
        Customer.cus_list.pop()
    def modify_Customer(self):
        for e in Customer.cus_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return

# PL
print("welcome to monika CRM")
def show_Customer(cus):
    print("Cust ID: ",cus.id,"Cust Name: ",cus.name,"Cust Age: ",cus.age,"Cust Mob: ",cus.mob)

while(1):
    ch = input("enter choice: 1 for Add Customer, 2 Search,3 Delete, 4 Modify, 5 Display all, 6 Exit:")

    #Add Customer
    if (ch=="1"):
        cus=Customer()
        cus.id=input("Enter Customer ID : ")
        cus.name=input("Enter Customer Name : ")
        cus.age=input("Enter Customer Age : ")
        cus.mob=input("Enter Customer Mob : ")
        cus.Add_Customer()

    #Search Customer
    elif (ch=="2"):
        cus=Customer
        cus.id=input("Enter Customer ID to Search : ")
        cus.Search_Customer(cus)
        show_Customer(cus)

    #Delete Customer
    elif (ch=="3"):
        cus=Customer()
        cus.id=input("Enter Customer ID to Delete : ")
        cus.Delete_Customer()
        show_Customer(cus)

    #Modify Customer1
    elif (ch=="4"):
        cus=Customer()
        cus.id=input("Enter Customer ID :")
        cus.name=input("Enter Updated Customer Name : ")
        cus.age=input("Enter Updated Customer Age : ")
        cus.Mob=input("Enter Updated Customer Mob : ")

    #Display All
    elif (ch=="5"):
        for i in Customer.cus_list:
            show_Customer(i)

    #Exit
    elif (ch=="6"):
        print("Thanks")
        break
    else:
        print("Invalid Choice")