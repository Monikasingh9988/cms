"Customer Management System"
# BLL:Business Logic Layer

id_list = []
name_list = []
age_list = []
mob_list = []
gender_list = []
date_of_birth_list = []
email_list = []
state_list = []
city_list = []

def Add_Customer(id, name, age, mob, gender, date_of_birth, email, state, city):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)
    gender_list.append(gender)
    date_of_birth_list.append(date_of_birth)
    email_list.append(email)
    state_list.append(state)
    city_list.append(city)
    return
def Search_Customer(id):
    index=id_list.index(id)
    return index
def Delete_Customer(id):
    i=id_list.index(id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)
    gender_list.pop(i)
    date_of_birth_list.pop(i)
    state_list.pop(i)
    city_list.pop(i)

def Modify_Customer(id, name, age, mob, gender, date_of_birth, state, city):
    i = id_list.index(id)
    name_list[i] = name
    age_list[i] = age
    mob_list[i] = mob
    gender_list[i] = gender
    date_of_birth_list[i] = date_of_birth
    state_list[i] = state
    city_list[i] = city

# PL:Persentation Layer
def Show_Customer(i):
    print("Customer ID:", id_list[i], "Customer Name:", name_list[i], "Customer Age:", age_list[i], "Customer Mob:", mob_list[i], "Customer Gender:", gender_list[i], "Customer Date_of_birth:", date_of_birth_list[i], "Customer Email:", email_list[i], "Customer State:", state_list[i], "Customer City:", city_list[i])

print("welcome to monika management system")
while(1):
    choice = input("Enter your choice:\n1. For Add Customer,\n2. Search Customer,\n3. Delete Customer\n4. Modify Customer,\n5. Display All Customer,\n6. Exit:")
    if(choice=="1"):            # Add New Customer
        id = input("Enter Customer ID:")
        name = input("Enter Customer Name:")
        age = input("Enter Customer Age:")
        mob = input("Enter Customer mob:")
        gender = input("Enter Customer Gender:")
        date_of_birth = input("Enter Customer Date_of_birth:")
        email = input("Enter Customer Email:")
        state = input("Enter Customer State:")
        city = input("Enter Customer City:")

        Add_Customer(id, name, age, mob, gender, date_of_birth, email, state, city)
        print("Customer Added Successfully")
    elif(choice=="2"):          #Search Customer
        id = input("Enter Customer ID to Search")
        i = Search_Customer(id)
        Show_Customer(i)
    elif(choice=="3"):         # Delete Customer
            id = input("Enter Cust Id to Delete:")
            Delete_Customer(id)
            print("Customer Deleted Successfully")
    elif(choice == "4"):      # Modify Customer
        id = input("Enter Customer Id to Modify:")
        name = input("Enter Cust updated name:")
        age = input("Enter Cust updated age:")
        mob = input("Enter Cust updated mob:")
        gender = input("Enter Customer Gender:")
        date_of_birth = input("Enter Customer Date_of_birth:")
        email = input("Enter Customer Email:")
        state = input("Enter Customer State:")
        city = input("Enter Customer City:")
        Modify_Customer(id, name, age, mob, gender, date_of_birth, email, state, city)
        print("Customer Modified Successfully")
    elif(choice=="5"):       # Display all Customers
        for i in range(len(id_list)):
            Show_Customer(i)
    elif(choice=="6"):      # Exit
        print("Thanks for using Monika CRM")
        break
    else:
        print("Incorrect Choice")




