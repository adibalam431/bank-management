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
        userdata = [
            i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
        ]
        if not userdata:
            print("No data found")
        else:
            amount = int(input("deposit amount :- "))
            if amount > 10000 or amount < 0:
                print("Either amount is too big or too low")
            else:
                userdata[0]["balance"] += amount
                Bank.__Update()
                print("Amount deposited successfully")

    # withdrew (balance update)
    def Withdrewmoney(self):
        account = input("Enter your account no. :-  ")
        pin = int(input("enter your pin :- "))
        userdata = [
            i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
        ]
        if not userdata:
            print("No data found")
        else:
            amount = int(input("withdrew amount :- "))
            if amount > 10000 or amount < 0:
                print("Either amount is too big or too low")
            elif userdata[0]["balance"] < amount:
                print("Insufficient funds")
            else:
                userdata[0]["balance"] -= amount
                Bank.__Update()
                print("Amount withdrew successfully")

    # details (account details)
    def Accountdetails(self):
        account = input("Enter your account no. :-  ")
        pin = input("enter your pin :- ")
        userdata = [
            i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
        ]
        if not userdata:
            print("No data found")
        else:
            print(f"Name : {userdata[0]["name"]}")
            print(f"Account No. : {userdata[0]["accountNo."]}")
            print(f"Balance : {userdata[0]["balance"]}")

    # details (account update)
    def Accountupdate(self):

        def Updatename():
            account = input("Enter your account no. :-  ")
            pin = input("enter your pin :- ")
            userdata = [
                i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
            ]
            if not userdata:
                print("No data found")
            else:
                newname = input("Enter your new name ")
                userdata[0]["name"] = newname
                Bank.__Update()
                print("Name updated successfully")

        def Updateage():
            account = input("Enter your account no. :-  ")
            pin = input("enter your pin :- ")
            userdata = [
                i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
            ]
            if not userdata:
                print("No data found")
            else:
                newage = input("Enter your correct age ")
                userdata[0]["age"] = newage
                Bank.__Update()
                print("Age updated successfully")

        def Updateemail():
            account = input("Enter your account no. :-  ")
            pin = input("enter your pin :- ")
            userdata = [
                i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
            ]
            if not userdata:
                print("No data found")
            else:
                newemail = input("Enter your new email ")
                userdata[0]["email"] = newemail
                Bank.__Update()
                print("Email updated successfully")

        def Updatepin():
            account = input("Enter your account no. :-  ")
            pin = input("enter your current pin :- ")
            userdata = [
                i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
            ]
            if not userdata:
                print("No data found")
            else:
                newpin = int(input("enter your new pin "))
                if len(str(newpin)) != 4:
                    print("pin not updated pin should be 4 digit")
                else:
                    userdata[0]["pin"] = str(newpin)
                    Bank.__Update()
                    print("Pin updated successfully")

        print("press 1 for updating name")
        print("press 2 for updating age")
        print("press 3 for updating email")
        print("press 4 for updating pin")

        response = int(input("tell your response :- "))
        if response == 1:
            Updatename()
        if response == 2:
            Updateage()
        if response == 3:
            Updateemail()
        if response == 4:
            Updatepin()

    def Accountdelete(self):
        account = input("Enter your account no. :-  ")
        pin = input("enter your pin :- ")
        userdata = [
            i for i in Bank.data if i["accountNo."] == account and i["pin"] == pin
        ]
        if not userdata:
            print("No data found")
        else:
            check = input("Press Y to delete account: ")
            
            if check == "y" or check == "Y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")


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
if check == 6:
    user.Accountdelete()
