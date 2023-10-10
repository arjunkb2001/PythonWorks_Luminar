numpep=int(input("how many people you wants to invite to the party: "))

def invitepep():

    if numpep < 10:
        for i in range(numpep):
            name = input(f"Enter the name of peoples {i + 1}: ")
            print(f"{name} has been invited.")
    else:
        print("Too many people")

invitepep()