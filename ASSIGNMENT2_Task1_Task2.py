#Task 1: Check if a Number is Even or Odd
print("--------- Task 1: Check if a Number is Even or Odd ---------\n")
v1=int(input("Enter the value to check whether it is even or odd: "))

if(v1%2==0):
    print(v1, "is an even number")
else:
    print(v1," is an odd number")

#Task 2: Check if a Number is Even or Odd
print("\n--------- Task 2: Sum of Integers from 1 to 50 Using a Loop ---------\n")
j=0
for i in range(1,51):
    j=j+i
print("Sum of Integers from 1 to 50 using loop is: ",j)