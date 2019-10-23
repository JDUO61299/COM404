print("how many zones must i cross?")
number = int(input())
print("crossing zones...")

zones = 0

while zones < number:
    print("... crossed zone " + str(number))
    number -=1

print("crossed all zones. Jumanji!")
