print("Welcome to Treasure Island")
print("Your mission is to find the treasure island.")
lr = input('Do you want to go left or right? Type "left" or "right" ').lower()
if lr == "right":
    print("You got run over by a bus")
elif lr == "left":
    lr = input("You come to a lake, do you want to wait or swim across? ").lower()
    if lr == "wait":
        print("You cross safely")
        lr = input("You can choose three doors, red, yellow or blue, which do you choose? ").lower()
        if lr == "yellow":
            print("You win")
        elif lr == "red" or lr == "blue":
            print("Wrong door")
        else:
            print("Wrong input")
    elif lr == "swim":
        print("You just couldn't wait could you")
    else:
        print("Wrong input")
else:
    print("Wrong input")