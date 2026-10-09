name = input("Enter your name:")
age = int(input("Enter your age:"))

student_id = input("Do you have an student ID? (y/n):")

print(f"=={name}==")
if(age < 5):
    print("Toddler")
    print(f"Ticket price is $0")
elif(5<= age <=17):
    print("Child/Teen")
    print("Ticket price is $10")
elif(18<= age <=64):
    if(student_id.lower() == "y"):
        print("Discounted Student")
        print("Ticked price is $12")
    else:
        print("Dtandard Audult")
        print("Ticket price is $18")
else:
    print("Senior Citizen")
    print("Ticket price is $8")