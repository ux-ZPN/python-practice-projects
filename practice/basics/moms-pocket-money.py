''' The Pocket Money Decider: Recreate the "Mom's pocket money" scenario. 
Ask the user to input an amount of money. 
Create an elif ladder with the following conditions:
If ₹10: Print "I will have a Chocobar"
.
If ₹50: Print "I will have Manchurian"
.
If ₹100: Print "I am going to McD"
.
If ₹500: Print "I am going to a 5-star Dhaba"
.
Else (if 0 or anything else): Print "I will stay hungry" '''


pm=input(int("enter amount of money"))
if pm == 10:
    print("I will have a Chocobar")
elif pm == 50:
    print("I will have Manchurian")
elif pm == 100:
    print("I am going to McD")
elif pm == 500:
    print("I am going to a 5-star Dhaba")
else:
    print("I will stay hungry")