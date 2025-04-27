print("Name:Maitrak Barot")
print("Roll no.:24BEE129")
def get_valid_integer():
    while True:
        user_input = input("Enter an integer: ")
        try:
            number = int(user_input)
            print(f"You entered a valid integer: {number}")
            return number
        except ValueError:
            print("Invalid input! Please enter an integer.")


get_valid_integer()
