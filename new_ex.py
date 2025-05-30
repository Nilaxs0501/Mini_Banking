import os
import datetime


Bank_accounts = {}
Transaction_history = {}


def date_time():
    return datetime.date.today()


def Customer_info():
    Name = input("Enter your Name: ")
    Nic_num = input("Enter your NIC number: ")
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    return [Name, Nic_num, Username, Password]


def Create_Customer_and_User():
    dt_info=date_time()
    customer = Customer_info()
    [name, nic, username, password ]=customer

    if username in Bank_accounts:
        print("Username already exists.")
        return

    Bank_accounts[username] = 0
    Transaction_history[username] = []

    with open("Customers_info.txt","a")as Customers_file:
        Customers_file.write(f"{ dt_info},{name},{nic}\n")

    with open("User_info.txt","a")as User_file:    
        User_file.write(f"{ dt_info},{username},{password}\n")
    print(f"Customer {username} created successfully.")
    print(f" {username} Welcome our Mini Bank ")


def View_All_Customers():
    if not os.path.exists("Customers_info.txt"):
        print("No customers found.")
        return

    with open("Customers_info.txt", "r") as Customers_file:
        lines =  Customers_file.readlines()
        if lines:
            print("Customer Records:")
            for line in lines:
                print(line.strip())
        else:
            print("No customer data available.")


def Deposit(username):
    dt_info=date_time()
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        Bank_accounts[username] += amount
        Transaction_history[username].append(f"Deposited {amount}")
        with open("Transaction.txt", "a") as file:
                file.write(f"{ dt_info},{username}: deposit:{amount}\n")

        print(f"Successfully deposited {amount}. New balance is {Bank_accounts[username]}")
    except ValueError:
        print("Please enter a valid amount.")


def Withdraw(username):
    dt_info=date_time()
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > Bank_accounts[username] :
            print("Insufficient balance.")
        elif Bank_accounts[username]['balance'] < 10000:
            print("Warning! Your Balance below RS.10000!")


        else:
            Bank_accounts[username] -= amount
            Transaction_history[username].append(f"Withdrew {amount}")
            with open("Transaction.txt", "a") as file:
                file.write(f"{ dt_info},{username}: withdraw :{amount}\n")

            print(f"Successfully withdrew {amount}. New balance is {Bank_accounts[username]}")

    except ValueError:
        print("Please enter a valid amount.")



def Customer_Creation():
    dt_info=date_time()
    try:
        username = input("Enter username for new account: ")
        if username in Bank_accounts:
            
            print(f"Wel come bank account creation '{username}' ")
        else:
            print(f"Username '{username}' already exists. Please choose a different username.")
            return

        balance = float(input("Enter initial deposit amount: "))
        if balance > 0:
            Bank_accounts[username] = balance
            Transaction_history[username] = [f"Initial deposit: {balance}"]
            print(f"Account created successfully. Welcome, {username}!")
            print(f"New balance is: {balance}")
            with open("Transaction.txt", "a") as file:
                file.write(f"{ dt_info},{username}:Initial deposit: {balance}\n")

        else:
            print("Invalid deposit amount. Must be greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the deposit amount.")

def get_transaction_history(username):
    username = input("Enter username for new account: ")
    if username in Transaction_history:
        Transaction_history = get_transaction_history(username)
        return Transaction_history[username]
    else:
        return f"No transaction history found for user '{username}'."
        
def Change_password(): 
    current= input("Enter your password: ")     
    with open("User_info.txt","r")as New_file:    
                for line in New_file:
                    words= line.strip().split(',')
                    if words[2]== current:
                        print("Create New Password")
                        new = input("Enter your  New Password: ")
                        if len(new)>6:
                            print("You Must give eligible Number is < 6 ")
                        elif len(new)<6 and len(new)==6:
                            with open("User_info.txt","a")as file:
                                file.write(f"{new}\n")
                                print(f"Created your New Password {new}")

#============================= ADMIN MENU====================================
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Create New Customer")
        print("2. Add New Customer Account")
        print("3. Deposit to Customer Account")
        print("4. Withdraw from Customer Account")
        print("5. View All Customers")
        print("6. View Transaction History")
        print("7. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            Create_Customer_and_User()
        elif choice == '2':
            Customer_Creation()
        elif choice == '3':
            user = input("Enter username: ")
            if user in Bank_accounts:
                Deposit(user)
            else:
                print("User not found.")
        elif choice == '4':
            user = input("Enter username: ")
            if user in Bank_accounts:
                Withdraw(user)
            else:
                print("User not found.")
        elif choice == '5':
            View_All_Customers()
        elif choice == '6':
            user = input("Enter username: ")
            if user in Bank_accounts:
                print(Transaction_history)

            else:
                print("User not found.")
        elif choice == '7':
            print("Logging out from admin account.")
            break
        else:
            print("Invalid choice. Please try again.")

#============================ CUSTOMER MENU===================================
def customer_menu(username):
    while True:
        print(f"\nWelcome {username}")
        print("1. View balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View Transaction History")
        print("5. Change  your Password")
        print("6. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            print(f"Your balance is: {Bank_accounts[username]}")
        elif choice == '2':
            Deposit(username)
        elif choice == '3':
            Withdraw(username)
        elif choice == '4':
            print(Transaction_history)
        elif choice == '5':
            Change_password()
        elif choice == '6':
            print(f"Logging out {username}.")
            break
        else:
            print("Invalid choice. Please try again.")

#============================ MAIN FUNCTION ===============================
def main():
    while True:
        print("\nWelcome to Mini Banking System")
        print("1. ===========Admin Login===========")
        print("2. ===========Customer Login========")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if password == "1234" and username == "admin":
                with open("User_info.txt","a")as User_file:    
                    User_file.write(f"{username},{password}\n")
                    print("Welcome Admin Our Banking System ")
                admin_menu()
            else:
                print("Invalid login please try again.")
        elif choice == '2':
            username = input("Enter your username: ")
            with open("User_info.txt","r")as New_file:    
                for line in New_file:
                    words= line.strip().split(',')
                    if words[1]== username:
                        customer_menu(username)
                break

        elif choice == '3':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()