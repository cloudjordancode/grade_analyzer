
try:
    bill = float(input("Enter the bill amount: $"))
    if bill < 0:
        print("Bill amount can't be negative.")
        exit()
        if bill == 0:
            print("Nothing to tip on.")
            exit()
except ValueError:
    print("\nError. Please enter a number. (e.g. 45.99): ")
    print("Exiting Program")
    exit()

try:
    tip_rate = float(input("Enter tip percentage (e.g. 20): "))
    if tip_rate < 0:
        print("Tip percentage can't be negative.")
        exit()
        if bill == 0:
            print("Nothing to tip on.")
            exit() 
except ValueError:
    print("\nError. Please enter a number (e.g. 20) ")
    print("Exiting Program")
    exit()

tip = bill * (tip_rate / 100)
total = bill + tip

print(f"Tip: ${tip:.2f}")

print(f"Total: ${total:.2f}")
