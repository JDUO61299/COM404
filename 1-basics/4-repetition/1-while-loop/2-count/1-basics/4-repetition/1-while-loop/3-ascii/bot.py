print("How many bars should be charged?")
bars = int(input())

charged = 0

while charged < bars:
    print("charging:")
    charged += 1
    print("█" * (charged))

print("the battery is fully charged!")