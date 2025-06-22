def countdown():
    counter = 5
    while counter > 0:
    print(counter)
    counter -= 1
    print("Go!")

def get_age():
    age = input("Enter your age: ")
    while not age.isdigit():
        print("Invalid input!")
    print(f"Age: {int(age)}")

countdown()
get_age()
