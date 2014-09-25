import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
def take_order():
    preferences = {}
    for k, v in questions.iteritems():
        cus_ans = raw_input(v)
        if cus_ans == 'yes' or 'y':
            preferences[k]=True
        else:
            preferences[k]=False
    return preferences

def make_order(preferences):
    drink = []
    for k, v in preferences.iteritems():
        if v == True:
            drink.append(random.choice(ingredients[k]))
    return drink

if __name__ == '__main__':
    print make_order(take_order())
