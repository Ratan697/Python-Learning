import random
secret_number = random.randint(1,100)
print("===Guess The Number Game===")
print("      ====RULES====")
print("1.Maximum 5 attempts")
print("2.Guess number in between 1-100\n")
print("****Let's Begin****")
i = 0
counter = 0
while(i<5):
    print(f"==Attempt {i+1} of 5==")
    num = int(input("Enter the number:"))
    if(num>secret_number):
        print("Too high! Go lower.")
    elif(num<secret_number):
        print("Too low! Go higher.")
    elif(num == secret_number):
        print(f"Congratulations! You guess the correct number in {i+1} attempts")
        counter += 1
        break
    i += 1
if(counter == 0):
    print(f"Game Over! You ran out of attempts. The number was {secret_number}.")