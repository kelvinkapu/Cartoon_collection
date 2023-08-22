def roll_call_dwarves(items):
    # items=[]
    for i in range(len(items)):
        # print(i)
        print(f"{i+1}. {items[i]}")
# print(roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"]))     

def summon_captain_planet(planeteer_calls):
    # print(planeteer_calls.upper)
      return [item.title()+'!' for item in planeteer_calls]

# print(summon_captain_planet(["earth", "wind", "fire", "water", "heart"]))
def long_planeteer_calls(words):
    #  for (len(word)>4) in words print (True)
    sorted_list=sorted(words, key=len, reverse=True)
    for word in sorted_list:
        if len(word)>4:
            return True
        else:
            return False
# print(long_planeteer_calls(["two","industrious", "go", "bop"]))

def find_the_cheese(foods):
    cheese=["cheddar", "gouda","camembert"]
    # eat=set(foods)
    for food in foods:
        if food in cheese:
            return food
        else:
            None


    # if (cheese & eat) = cheese
    
    # return ','.join(cheese & eat)
    # cheese = eat
    # for food in foods:
    #     foods.find(cheese)
print(find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"]))
