
sender_name = input("Enter your Name: ")
item = input("Enter the type of item: ")


isFragile = input("Is the item fragile? (True/False): ") == "True"
weight = float(input("Input the weight in kg: "))
distance = float(input("Input the distance in km: "))
isExpress = input("Is it Express? (True/False): ") == "True"
isInternational = input("Is International? (True/False): ") == "True"

# Calculating the Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

#Evaluating the total cost based on the conditions provided:
if weight <= 2.0 and distance <= 100 and not isExpress and not isInternational:
    total = 0.00
elif isInternational and isExpress:
    total = (base_cost * 1.40) + 50
elif isExpress or (isInternational and weight > 20):
    total = (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
    total = base_cost + 30
else:
    total = base_cost




print("Sender Name: ", sender_name)
print("Type of Item: ", item)
print("Weight (kg): ", weight)
print("Distance (km): ", distance) 
print("Total Cost: ", total)

