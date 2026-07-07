from classes import Bank
data =[] #store all the account details in this list

def create_account(x,y,z,data): #this method creates a new account and adds it to the data list
    bank = Bank(0)
    data.append([x,y,z,bank])
    return bank

def login(X,Y,Z,data): #this method checks if the account number, username and password entered by the user matches with the account details stored in the data list
    for account in data:
        if X ==account[0] and Y ==account[1] and Z ==account[2]:
            print("logging in")
            return True
        
        else:
            print("Incorrect username or password")
            return False    
    