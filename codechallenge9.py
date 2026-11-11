#Target1
monthly = int(input("Input Monthly: "))
principal = 41.67
rem_ball = 912.234234234234

print(monthly, "|", principal, "|", rem_ball)
print(f"{monthly}\t\t | {principal}\t\t | {round(rem_ball, 2)}")













print()
#Target2

rows = int(input("Enter the row size for the pattern: "))
for x in range(1, rows + 1):  
    for y in range(rows  - x):  
        print(" ", end=" ")
    for j in range(1, x + 1):  
        print(j, end=" ")
    for c in range(x - 1, 0, -1):  
        print(c, end=" ")
    print()


print()
#Target3

n = 5

for x in range(n):
    for y in range(n):
        if x == 0 or x == n - 1 or x + y == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
