print("how many miles must i travel before i reach the secret base?")
distance = int(input())
length = 0

while length < distance:
    print("i will count the miles...i have " + str(distance) + str(" miles before i reach the base"))
    distance -=1

print("i have arrived at the secret headquarters of the MIB")
print("it is time to sneak in")