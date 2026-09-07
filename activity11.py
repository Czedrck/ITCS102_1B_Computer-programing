#import demo	
import getpass

username = "Cedrick"
password = "KaninBuseng"

u = input("Input Username ---> ")
p = getpass.getpass("Input Password ---> ")


if u == username or p == password :
        print("username and password is correct")
else :
        print("access denied")

