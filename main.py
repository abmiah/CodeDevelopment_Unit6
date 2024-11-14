def message():
    name = input("Enter your name: ")
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
        print("You didn't enter your name. But that's okay. I'll still say hello to you.")

message()
