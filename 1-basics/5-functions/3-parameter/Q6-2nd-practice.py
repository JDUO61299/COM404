def is_league_united(hero1,hero2):
    if hero1 == "superman" and hero2 == "wonderwoman":
        return True
    elif hero1 == "wonderwoman" and hero2 == "superman":
        return True
    else:
        return False

def decide_plan(hero1,hero2):
    if is_league_united(hero1,hero2) == True:
        return "time to save the world!"
    else:
        print(" We must unite the league!")   

def run():
    firstHero = input("enter name of first hero ")
    secondHero = input("enter name of second hero ")
    word = input("enter the word league or plan ")
    if word == "league":
        print(is_league_united(firstHero,secondHero))
    elif word == "plan":
        print(decide_plan(firstHero,secondHero))
    else:
        print("Invalid command. Please try again" )

run()
