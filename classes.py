class Bank:
    def __init__(self,balance):
        self._balance = balance # instance attribute to store balance
        self.history = [] #stores complete transaction history of the account
   
    @property #getter method for balance
    def balance(self):
        return self._balance
    @balance.setter #setter method for balance
    def balance(self,value):
            self._balance = value    

    def Credit(self,amount): #this method credits amount to account and adds transaction to history
        if amount >0:
            self._balance+= amount 
            print("Amount credited succesfully")
            self.history.append(f"Credited: {amount} Rs")

        else:
            print("Insufficient amount") 
    
    def Debit(self,Amount): #this method debits amount from account and adds transaction to history
        if Amount >0 and self._balance >=Amount:
            self._balance-= Amount
            print("amount debited succesfully")
            self.history.append(f"Debited: {Amount} Rs")

        elif Amount <0:
            print("Insufficient amount") 
            
        elif self._balance <Amount:
            print("Insufficient Balance") 
    
    def show_History(self): #this method displays the complete transaction history of the account 
        print("_____Transaction History_____")
        for transaction in self.history:
            print(transaction)
    
    def check_balance(self): #this method displays the current balance of the account
        print(f"Balance:{self.balance}Rs")          

    


