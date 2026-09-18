

u = input("Please enter username to log in: ")
p = input("Please enter password to log in: ")

if u == "Cedrick" or p == "Lipata" :
    print()
    print("---------------------- [W E L C O M E] -----------------------")
    print("------------ Welcome user please fill each blank ------------")
    print()
    
    age = int(input("Enter Age : "))
    isEmployed = bool(input("Are you currently employed : "))
    credits = eval(input("Credit Score History : "))
    annual = eval(input("How much is your annual income : "))
    collateral = bool(input("Do you have any collateral : "))

    base_rate = 0.0

    if age >= 21 and isEmployed == True:
        print("Passed for baseline eligibility")
        if credits >= 750 :
            print("Your credit score is above 750")
            if annual >= 100000:
                print("You have a High Annual Income")
                base_rate = 4.5
                print("HI, Your interest rate is ", base_rate)
            else :
                base_rate = 5.0
                print("Hi, Your interest rate is ", base_rate)

    elif credits >= 600 and credits < 750:
        if collateral == True:
            base_rate = 7.0
            print("Hi, Your interest rate is ", base_rate)

        elif annual < 40000:
            base_rate = 9.5
            print("Hi, Your interest rate is ", base_rate)

        else:
            base_rate = 8.0
            print("Hi, Your interest rate is ", base_rate)
            

    else:
        print("Reject, Failed baseline eligibility")
            
else:
    print("Login failed. Program stopped.")
    
print()
print("------------------- COMPUTATION COMPLETED -------------------")



    
    
    
