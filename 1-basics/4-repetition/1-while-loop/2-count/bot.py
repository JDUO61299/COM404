print("how many live cables should i avoid?")
live = int(input())

avoid = 0

while avoid < live:
    print("avoiding...")
    avoid += 1
    print("...Done! " + str(avoid) + " live cables avoided!")

print("all the live cables avoided!")

