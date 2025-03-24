while True:
    print("Hello, what can I call you?")
    a = input()
    print(f"Hello {a}")
    b = input("How are you feeling today(good or bad)? ")
    c=b.lower()
    if c=="good":
        print("Good to hear that.")
    elif c=="bad":
        print("Oh! I hope things get better soon.")
    else:
        print("Sometimes its hard to feelings in words")
    print(f"Nice meeting you {a},Goodbye")
    e = input("Do you want it to repeat?(Yes/no) ")
    f=e.lower()
    if f=="no":
        break
    

