name  = input("Enter your name: ")
while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age: "))

while age <0:
    print("Your age must be greater than or equal to zero")
    age = int(input("Enter your age: "))
print(f"Your name is {name} and your age is {age}")

for i in range(1,11,2):
    print(i)

name = "tony stark"

for letter in name:
    print(letter, end=" ")