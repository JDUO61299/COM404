print("how many numbers should i sum up?")
numbers = int(input())

count = 0
total = 0
while count < numbers:
    count +=1 
    print(" please enter number " + str(count) + " of " + str(numbers))
    userNum = int(input())
    total += userNum

print("the answer is " + str(total))