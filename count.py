try:
    amount = int(input("amount: "))
    result = 1000 / amount
    print(result)

except ValueError:
    print("please enter a number")

except ZeroDivisionError:
    print("Amount cant be zero")

try:
    with open("readme.md", "a") as f:
        print("Opened successfully.")
        text = input("Enter text to update: ")
        f.write(text + "\n")

except FileNotFoundError:
    print("File is missing.")