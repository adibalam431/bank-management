import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # path & error handle
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"an exception occur as {err}")

    @staticmethod  # write method (update)
    def __Update():
        with open(Bank.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod  # create method (account number generate)
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    # create method (accountgenerate)
    def Createaccount(self):
        info = {
            "name": input("Name :- "),
            "age": int(input("Age :- ")),
            "email": input("email :- "),
            "pin": input("pin :- "),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0,
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("You can not create account")
        else:
            print(f"\n\n\nacccount has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")

            print("save your account no. & account details")
            Bank.data.append(info)
            Bank.__Update()

    # deposit (balance update)
    def Depositmoney(self):
        account = input("Enter your account no. :-  ")
        pin = input("enter your pin :- ")
        userdata = [i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin]
        if userdata == False:
            print("No data found")
        else:
            amount = int(input("deposit amount :- "))
            if amount >10000  or amount < 0:
                print("Either amount is too big or too low")
            else:
                userdata[0]["balance"]+=amount
                Bank.__Update()
                print("Amount deposited successfully")

    # withdrew (balance update)
    def Withdrewmoney(self):
        account = input("Enter your account no. :-  ")
        pin = input("enter your pin :- ")
        userdata = [i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin]
        if userdata == False:
            print("No data found")
        else:
            amount = int(input("withdrew amount :- "))
            if amount >10000  or amount < 0:
                print("Either amount is too big or too low")
            elif userdata[0]["balance"]<amount:
                print("Insufficient funds")
            else:
                userdata[0]["balance"]-=amount
                Bank.__Update()
                print("Amount withdrew successfully")

    # details (account update)
    def Accountdetails(self):
        account = input("Enter your account no. :-  ")
        pin = input("enter your pin :- ")
        userdata = [i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin]
        if userdata == False:
            print("No data found")
        else:
            print("hey")
user = Bank()
print("press 1 for creating an account")
print("press 2 for depositing money in the bank account")
print("press 3 for withdrawing money from bank account")
print("press 4 for bank account details")
print("press 5 for updating bank account details")
print("press 6 for deleting bank account")

check = int(input("tell your response :- "))
if check == 1:
    user.Createaccount()

if check == 2:
    user.Depositmoney()
    
if check == 3:
    user.Withdrewmoney()
    
if check == 4:
    user.Accountdetails()
    
if check == 5:
    user.Accountupdate()
