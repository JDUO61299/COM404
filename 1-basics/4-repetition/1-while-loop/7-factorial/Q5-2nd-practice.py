health = 100
print("Your health is 100%. Escape is in progress...")

for count in range(0,5,1):
    print("…Oh dear, who is that?")
    userResponse = input()
    if userResponse == "smilers bot":
        health -= 20
        print("time to jam out of here")
    elif userResponse == "hacker":
        health += 20
        print( "Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")

print("escaped! health is " + str(health))