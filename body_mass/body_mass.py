# The program calculates a person's body mass index


# Entry of body weight in kg
weight= float (input ("Enter your body mass - kg :  "))

# Enter the height in cm
height=float(input("Enter the height -cm :    "))

# Calculation of body mass index
indeks = weight /((height/100)**2) 
#the result
print("Body mass is : " , indeks )
