class Bank:
    
    

user =  Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money in the bank account")
print("press 3 for withdrawing the money from bank account")
print("press 4 for bank account details")
print("press 5 for updating bank account details")
print("press 6 for deleting bank account")

check = int(input("tell your response :- "))
if check == 1:
    user.Createaccount()