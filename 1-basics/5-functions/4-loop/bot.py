
def cross_bridge(distance):

    for count in range(distance):
        print("crossed step")

    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print( "we must keep going!")

cross_bridge(6)