#For stopping program execution for some time
import time

print("Please insert Your ATM Card")

#for card processing
time.sleep(5)

password = 1234

#taking atm pin from user
pin = int(input("Enter your ATM pin: "))

#user account balance
balance = 5000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == Balance
			2 == Withdraw Balance
			3 == Deposit Balance
			4 == Exit
			"""
              )

        try:    
             #taking an option from user
            option = int(input("Please Enter your choice: "))
        except:
            print("Please Enter your valid option: ")
        
        #for option 1        
        if option == 1:
            print(f"Your current balance is {balance}.")
                                     
        if option == 2:

            withdraw_amount = int(input("Please Enter Withdraw Amount "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your Account.")

            

            print(f"Your updated balance is {balance}.")

            

        if option == 3:

            deposit_amount = int(input("Please Enter Deposit Amount: "))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your Account.")



            print(f"Your updated balance is {balance}")



        if option == 4:

            break


else:
    print("Wrong pin !!! Please try again")
