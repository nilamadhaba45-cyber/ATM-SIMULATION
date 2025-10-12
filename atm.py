print("WelCome to ATM Simulation")

#step 1 : ATM and user detail Setup

user_balance=10000
atm_notes={2000:5,500:20,100:25} #note:denomination:count
Correct_pin=1010
#check transaction history
transactions=[]

#step 2 : ATM Verification (3 attempts pin)
pin_ok=False
for attempt in range(3):
    pin=int(input("Please Enter Your Pin = "))
    if pin == Correct_pin:
        pin_ok = True
        break
    else:
        print("You Enterd Wrong Pin, Try Again.")
if not pin_ok:                                                  #pin_ok=False, execute that
    print("Your Card is Blocked due 3 attempts is wrong pin !")
else:                                                           #pin_ok=true, execute that
    while True:                                                 #loop until exit
        print("\n ====ATM Menu====")                                #step 3 : menu option start choose your activity an atm
        print("1. Check Balance.")
        print("2. Withdrawl.")
        print("3. Deposit")
        print("4. Transaction History")
        print("5. Exit.")
        choice=int(input("Enter your Choice = "))                   #ask to user What you active in atm. choose number then execute
        if choice==1:                                               #choosing 1
            print(f"Your Account Balance = {user_balance}")
        elif choice==2:                                               #choosing 2
            amount=int(input("Enter your withdrawl ammount = "))    
            if amount>user_balance:
                print("sorry insuficient balance in your account.")
            elif amount%100!=0:                                     
                print("Enter amount in multiplies of 100.")
            else:
                '''user_balance-=amount
                transaction.append(f"Withdrawn:{user_balance}")
                print(f"Withdrawal successful! Remaining balance: ₹{user_balance}")'''

                withdraw_note={}                                    #withdrawl notes store
                remaining=amount
                for note in atm_notes:
                    if remaining >= note and atm_notes[note]>0:       #accept Cnodition then go next line not accept then go next note 
                        needed=remaining//note
                        if needed <= atm_notes[note]:
                            withdraw_note[note]=needed
                            remaining -= needed*note
                        else:
                            withdraw_note[note]=atm_notes[note]
                            remaining -= atm_notes[note]*note
                if remaining==0:                                       #if amount can be dispensed fully
                    print("\n💵 Please collect your cash:")                    
                    for note, count in withdraw_note.items():
                        if count>0:
                            print(f"{note} X {count}")
                            atm_notes[note] -=count
                    user_balance -= amount
                    transactions.append(f"Withdrawn: {amount}")
                    print(f"Your Remaining Balance = {user_balance}")
                else:
                    print("Sorry insufficient note")
        elif choice==3:             #exit                                    #chossing 3
            deposit = int(input("Enter amount to deposit: ₹"))
            if deposit > 0:
                user_balance += deposit
                transactions.append(f"Deposited: ₹{deposit}")
                print(f"₹{deposit} deposited successfully. New balance: ₹{user_balance}")
            else:
                print("⚠️ Enter a valid amount.")
        elif choice == 4:
                print("\n Transaction History:")
                if len(transactions) == 0:
                    print("No transactions yet.")
                else:
                    for t in transactions:
                        print("-", t)
        elif choice == 5:
                print("\n👋 Thank you for using Python ATM!")
                exit()
        else:
                print("⚠️ Invalid choice! Please select between 1–5.")                 
    
                                                                                     
    

