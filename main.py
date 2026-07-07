from Account import create_account,data
from Account import login
while True:
    print("____MENU____") #displays the main menu of the program
    print("1)Create Account\n2)Exit")
    a = int(input("Enter choice:")) 

    if a==1: #this option allows the user to create a new account
        x = int(input("Create account number:"))
        y = (input("Create Username:"))
        z= (input("Create password:"))
        bank =create_account(x,y,z,data) #this method creates a new account and adds it to the data list
        
        while True:
            print("____MENU____") #displays the menu after creating an account
            print("1)Login\n2)Exit")
            b = int(input("Enter choice:"))

            if b==1: #this option allows the user to login to their account
                X = int(input("Enter account number:"))
                Y= (input("Enter Username:"))
                Z= (input("Enter password:"))

                if login(X,Y,Z,data): 
                    while True:
                        print("____MENU___") #displays the menu after logging in
                        print("1)credit money\n2)debit money\n3)view Transaction History\n4)Check Balance\n5)Exit")
                        c = int(input("Enter choice:"))

                        if c==1: #this option allows the user to credit money to their account
                            amount = int(input("Enter amount:"))
                            account_number =int(input("Enter account number:"))
                            for account in data:
                                if account[0] == account_number:
                                    bank = account[3]
                                    bank.Credit(amount)
                                    break 

                                else:
                                    print("Account not found")
                        
                        elif c==2: #this option allows the user to debit money from their account
                            Amount = int(input("Enter Amount:"))
                            account_number =int(input("Enter account number:"))
                            for account in data:
                                if account[0] == account_number:
                                    bank = account[3]
                                    bank.Debit(Amount)
                                    break 

                                else:
                                    print("Account not found")

                        elif c==3: #this option allows the user to view their transaction history
                            account_number =int(input("Enter account number:"))
                            for account in data:
                                if account[0] == account_number:
                                    bank = account[3]
                                    bank.show_History()
                                    break 

                                else:
                                    print("Account not found") 

                        elif c==4: #this option allows the user to check their account balance
                            account_number =int(input("Enter account number:"))
                            for account in data:
                                if account[0] == account_number:
                                    bank = account[3]
                                    bank.check_balance()
                                    break

                                else:
                                    print("Account not found")

                        elif c==5: #this option allows the user to exit the program
                            print("Exiting...")
                            break

                        else: #this option handles invalid choices entered by the user
                            print("Invalid choice")

            elif b==2: #this option allows the user to exit the program
                print("Exiting...")
                
                
            else: #this option handles invalid choices entered by the user
                print("Invalid choice")

    elif a==2: #this option allows the user to exit the program
        print("Exiting...") 
        break

    else: #this option handles invalid choices entered by the user
        print("Invalid choice")  




