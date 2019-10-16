
def sum_weights(bopWeight, beepWeight):
    total = bopWeight+beepWeight
    return total

def calc_avg_weight(bopWeight, beepWeight):
    average = (bopWeight+beepWeight)/2
    return average

def run():
    print("what is bop's weight?")
    bopWeight = int(input())

    print("what is beep's weight?")
    beepWeight = int(input())

    print("what would you like to calculate (sum or average)")
    calculate = input()

    if calculate == "sum":
        sumWeights = sum_weights(bopWeight, beepWeight)
        print(("the combined weight of bop and beep is ")  +  str(sumWeights))
    else:
        average = calc_avg_weight(bopWeight, beepWeight)
        print(("the average weight of bop and beep is ")  +  str(average))

run()
