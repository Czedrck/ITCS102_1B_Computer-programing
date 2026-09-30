

age = int(input("Enter your Age"))
rev = float(input("Enter your monthly revenue"))
cc = int(input("Enter your credit score"))
yrs_b = int(input("Years in Business"))
has_defaults = bool(input("Default History"))
collateral = input("Collateral Name")
c_value = float(input("Collateral Value"))

max_limit = 0
base_fee = 0.0
#baseline

if age >= 21 and yrs_b >= 2 and has_defaults == False:
    print("BASELINE REQUIREMENT PASSED")

    if cc >= 720: #tier1
        max_limit = rev * 3
        print("HIGH CREDIT SCORE HISTORY")
        if rev >= 50000:
            base_fee = max_limit * 0.015
            print("BASE FEE RATE IS", base_fee)
        else: 
            base_fee = max_limit * 0.025
            print("BASE FEE RATE IS", base_fee)

        if c_value >= max_loan :
            print("COLLATERAL", collateral, "ACCEPTED")
        else :
            print("COLLATERAL NOT ACCEPTED")

        surcharge = max_loan * base_fee
        if c_value % 5000 != 0:
            surcharge += 0 

    elif cc <= 720 and cc < 720: #tier2
        max_loan = rev * 1.5
        print("MAX LOAN IS SET TO ", max_loan)
        if yrs_b >= 5:
            base_fee = max_loan * 0.02
            print("BASE FEE RATE IS ", base_fee)
        else :
            base_fee = max_loan * 0.035
            print("BASE FEE RATE IS ", base_fee)

        if c_value >= max_loan :
            print("COLLATERAL", collateral, "ACCEPTED")
        else :
            print("COLLATERAL NOT ACCEPTED")

    elif cc < 620:
        print("CREDIT SCORE TOO LOW")
    else : 
        print("NOT TIER 1")

else :
    print("REJECTED: HIGH RISK APPLICATION OR INELEGIBLE OWNER")







                





















