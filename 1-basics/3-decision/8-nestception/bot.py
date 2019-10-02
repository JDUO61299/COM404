where = input("where should i look?")
if where == "in the bedroom":
    print("where in the bedroom should i look?")
    bedroom = input()
    if bedroom == "in the cupboard":
        print("found some mess but no battery")

if where == "in the bathroom":
    print("where should i look in the bathroom?")
    bathroom = input()
    if bathroom == "in the bathtub":
        print("found a rubber duck but no battery")

if where == "in the lab":
     print("where in the lab should i look?")
     lab = input()
     if lab == "on the table":
        print("yes! i found my battery")
