#for stopping program execution for some time


import time
print("please insert your card")
#for card processing
time.sleep(5)

password= 12345
#taking atm pin from user
pin=int(input("enter your atm pin"))
#user acount balance
balance =10000
#checking pin is valid or not
if pin==password:
    #loop will run user get free
    while True:
        print("""
        1== balance
        2== withdraw balance 
        3== deposit balance 
        4== exit 
        """)
        try:
            option = int(input("please enter your choise"))
        except:
            print("please enter valid option")
        if option == 1:
            print(f"your current balance is {balance}")
            print("=====================================")
            print("=====================================")
        if option ==2:
            withdraw_amount=int(input("please enter withdraw_amount"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print("=====================================")
            print("=====================================")
            print(f"your updated balance is {balance}")
            print("=====================================")
            print("=====================================")
        if option ==3:
            deposit_amount =int(input("please enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount}is credit to your account")
            print("=====================================")
            print("=====================================")
            print(f"your update balance is {balance}")
            print("=====================================")
            print("=====================================")
        if option ==4:
            break
else:
            print("wrong pin please try again")









