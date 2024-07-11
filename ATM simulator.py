print("\t\t\t\t Welcome to XYZ Bank \n\nInsert your card")
password = 1234
pin=int(input("Enter your four digit pin : "))
balance=10000

if (pin == password):
        print("\t\t\t\t****Menu****\n")
        print("\t\t\t\t1.Check Balance\n")
        print("\t\t\t\t2.Withdraw\n")
        print("\t\t\t\t3.Deposit\n")
        choice = int(input("Enter your choice : "))

        if(choice == 1):
            print("Balance : Rs.", balance)
        
        elif(choice == 2):
            withdraw_amt = int(input("Enter the withdrawal amount : Rs."))
            balance = balance + withdraw_amt
            print("Balance : Rs.", balance)
        
        elif(choice == 3):
            deposit_amt = int(input("Enter the deposit amount : Rs."))
            
            if(deposit_amt < balance):
                balance = balance - deposit_amt
                print("Balance : Rs.", balance)

            else:
                 print("Insufficient Balance")
        
        else:
             print("Wrong input!!")


else:
    print("Incorret pin.. Try again!!")
