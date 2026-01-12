from pandas.io.sas.sas_constants import page_bit_offset_x64

print(123_456_789_10) #this is a number that is easier to read

# type check
print(type("123"))
print(type(123))
print(type(1.34))
print(type(True))

# type cast int() str() bool() float()
print(type(float(123)))

print(5/3) #float
print(5//3) #int
print(2 ** 3) #2 to power of 3

print(round(5/3))
print(round(5/3,2))

score=5
classroom=5.8
winning=True
print(f"Your score is {score}, your classroom is {classroom}, your winning is {winning}")

print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = int(input("Percentage of tip?"))
pax= int(input("How many people to split the bill"))
amount = bill* (1+(tip / 100))  / pax
print(f"Amount per pax is ${round(amount,2)}")


