print("WelCome to ATM Simulation")

#step 1 : ATM and user detail Setup

user_balance=10000
atm_notes={2000:5,500:20,100:25} #note:denomination:count
Correct_pin=1010

#step 2 : ATM Verification (3 attempts pin)
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
    for _ in range(100):                                        #loop until exit
        print("\n ====Menu====")                                    #step 3 : menu option start choose your activity an atm
        print("1. Check Balance.")
        print("2. Withdrawl.")
        print("3. Exit.")
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
                            remaining -= atm_notes[note]
                if remaining==0:                                       #if amount can be dispensed fully
                    print("Please Collect Your Cash and Take your card")
                    for note, count in withdraw_note.items():
                        if count>0:
                            print(f"{note} X {count}")
                            atm_notes[note] -=count
                    user_balance -= amount
                    print(f"Your Remaining Balance = {user_balance}")
                else:
                    print("Sorry insufficient note")
        elif choice==3:             #exit                                    #chossing 3
            print("Thank you for using ATM And Visit Again")
            break
        else:
            print("Invaid Coice, Try Again")
                                                                                     
    

