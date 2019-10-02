bookCover = input("what type of cover does the book have?")
if bookCover == "soft":
    print("is the book perfect-bound?")
    perfect = input()
    if perfect == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

if bookCover == "hard":
    print("Books with hard covers can be more expensive!")





