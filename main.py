#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")
Bill = input("What was the bill total?\n")
Tip = input("How much tip would you like to giv?\n%")
NumPeople = input("How many people to split the bill?\n")
Bill = float(Bill)
Tip = float(Tip)
NumPeople = int(NumPeople)
Tip = Tip/100
Tip = Tip + 1

EachPersonBill = (Bill / NumPeople) * (Tip)
EachPersonBill = round(EachPersonBill, 2)
print(f"Each person should pay: {EachPersonBill}")
