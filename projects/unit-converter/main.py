
''' 
#function

def km_to_miles(km):
    return km * 0.621371
def miles_to_km(miles):
    return miles/0.621371
def kg_to_lbs(kg):
    return kg*2.20462
def lbs_to_kg(lbs):
    return lbs/2.20462
def c_to_f(c):
    return (c * 9/5) + 32
def f_to_c(f):
    return (f - 32) * 5/9

#code
print("Welcome to Unit Converter")
print("1.Convert Kelometers to miles")
print("2.Convert miles to Kelometers")
print("3.Convert kilograms to pounds")
print("4.Convert pounds to kilograms")
print("5.Convert Celsius to Fahrenheit")
print("6.Convert Fahrenheit to Celsius")

choice=int(input("Enter your choice (1-6): "))

if choice==1:
    km_input=float(input("Enter Distance in Kelometers :"))
    result=km_to_miles(km_input)
    print(f"{km_input} kilometers is equal to {result} miles")

elif choice==2:
    miles_input=float(input("Enter Distance in Miles :"))
    result=miles_to_km(miles_input)
    print(f"{miles_input} miles is equal to {result} kilometers")

elif choice==3:
    kg_input=float(input("Enter Weight in Kilograms :"))
    result=kg_to_lbs(kg_input)
    print(f"{kg_input} kilograms is equal to {result} pounds")

elif choice==4:
    lbs_input=float(input("Enter Weight in Pounds :"))
    result=lbs_to_kg(lbs_input)
    print(f"{lbs_input} pounds is equal to {result} kilograms")

elif choice==5:
    c_input=float(input("Enter Temperature in Celsius :"))
    result=c_to_f(c_input)
    print(f"{c_input} Celsius is equal to {result} Fahrenheit")

elif choice==6:
    f_input=float(input("Enter Temperature in Fahrenheit :"))
    result=f_to_c(f_input)
    print(f"{f_input} Fahrenheit is equal to {result} Celsius")
else:
    print("Invalid choice")
    
'''
import streamlit as st

# --- 1. YOUR FUNCTIONS (Exactly as you wrote them) ---
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9


# --- 2. STREAMLIT UI (Replacing your print/input menu) ---
st.title("My Unit Converter")

# Create a dropdown menu instead of typing 1-6
choice = st.selectbox("Select Conversion", [
    "Kilometers to miles", 
    "Miles to kilometers", 
    "Kilograms to pounds", 
    "Pounds to kilograms", 
    "Celsius to Fahrenheit", 
    "Fahrenheit to Celsius"
])

# Create a number box instead of using float(input())
user_input = st.number_input("Enter the value to convert:")

# --- 3. CONVERSION LOGIC ---
# This button replaces your terminal enter key
if st.button("Convert"):
    
    if choice == "Kilometers to miles":
        result = km_to_miles(user_input)
        st.success(f"{user_input} kilometers is equal to {result} miles.")
        
    elif choice == "Miles to kilometers":
        result = miles_to_km(user_input)
        st.success(f"{user_input} miles is equal to {result} kilometers.")
        
    elif choice == "Kilograms to pounds":
        result = kg_to_lbs(user_input)
        st.success(f"{user_input} kilograms is equal to {result} pounds.")
        
    elif choice == "Pounds to kilograms":
        result = lbs_to_kg(user_input)
        st.success(f"{user_input} pounds is equal to {result} kilograms.")
        
    elif choice == "Celsius to Fahrenheit":
        result = c_to_f(user_input)
        st.success(f"{user_input} Celsius is equal to {result} Fahrenheit.")
        
    elif choice == "Fahrenheit to Celsius":
        result = f_to_c(user_input)
        st.success(f"{user_input} Fahrenheit is equal to {result} Celsius.")