# import random
from pokemon_data_io import *
database = "DATA/Pokemon.csv"
db = open_file(database, "r")

Pokemon_data = load_raw_data(db)
Pokemon_data_indexed = parse_raw_data(Pokemon_data)
Pokemon_types_list = parse_pokemon_data(Pokemon_data_indexed)

answer = input("Howdy partner! Welcome to the Pokemon Deck Creator! Do you want to make a Pokemon deck? Please type yes or no.")
answer = fix_string_input(answer)
while answer != "Yes" or "No": # keeps looping till the answer is yes or no
    if answer == "Yes":
        print("Okay! Let's get started.")
        break
    if answer == "No":
        print("Goodbye!")
        exit()
    else:
        print("Please type yes or no.")
        answer = input('Would you like to make a deck?')
        answer = fix_string_input(answer)

deck_type = []# open list for user chosen_type

pokemon_types = Pokemon_types_list
pokemon_types = remove_brackets(pokemon_types)
pokemon_types = pokemon_types.replace('TypeA', ' ').strip()# takes TypeA out of the list

print('These are the types of Pokemon:', pokemon_types)  # presents the user the types of pokemon

while len(deck_type) < 1:# keeps the deck_type list under 2. repeats until a correct type is chosen
    chosen_type = input("What type of Pokemon would you like in your deck?")  # chosen_type is the pokemon type chosen by user
    chosen_type = fix_string_input(chosen_type)
    if chosen_type in Pokemon_types_list:
        print(" Okay! you chose", chosen_type, "!")
        deck_type.append(chosen_type)
    if chosen_type not in Pokemon_types_list:
        print("Please choose from the list.")

want_second_type = input("Would you like to choose a second type to add to your deck? Please type yes or no.")
want_second_type = fix_string_input(want_second_type)
while len(deck_type) < 2:# keeps types in deck_type under 3
    if want_second_type == "Yes":# if the user adds another type
        second_type = input("What secondary type would you like?")
        second_type = fix_string_input(second_type)
        if second_type in Pokemon_types_list:# verifies that this is a type in the data set
            print("You chose " + second_type + " as your second type of Pokemon!")
            deck_type.append(second_type)
            deck_type = remove_brackets(deck_type)
            deck_type = deck_type.split(' ')
            print("Please wait while we make your", deck_type[0], 'and', deck_type[1], "type deck.")
            break
        else:# repeats until a correct option is chosen
            print("Please choose from the list.")
    if want_second_type == "No":# the user only wants a single type deck
        deck_type = remove_brackets(deck_type)
        print("Please wait while we make your", deck_type, "type deck.")
        deck_type = [deck_type] # needs to be a list to work in the pokemon_with_common_types function or it will only work with two inputs
        break# jumps to the deck generator

pokemon_with_similar_types = pokemon_with_common_types(Pokemon_data_indexed, deck_type)

deck_list = []
#deck_list = deck_randomness(pokemon_with_similar_types, deck_list)
deck_list = randomize(pokemon_with_similar_types)

print("Here is your deck:")
print("#  Name   TypeA    TypeB   Total   HP   Attack   Defense   Sp.Atk   Sp Def   Speed   Generation   Legendary")
for pokemon in deck_list:
    print(*pokemon) # COOL STAR THING!!! its the same as just printing each part of the list. * = unpacking

deck_completed = input("Do you like the deck that has been created for you? Yes or No?")
deck_completed = fix_string_input(deck_completed)
while deck_completed != "Yes":
    if deck_completed == "No":
        try_again = input("I am sorry you are not happy with the deck I have created. Would you like me to try again? Yes or No?")
        try_again = fix_string_input(try_again)
        if try_again == "No":
            print("Okay, goodbye.")
            exit()
        if try_again == "Yes":
            print("Thank you for giving me another chance! I won't let you down!")
            new_deck_list = []
            new_deck_list = randomize(pokemon_with_similar_types)
            print("Here is your new deck:")
            print("#  Name   TypeA    TypeB   Total   HP   Attack   Defense   Sp.Atk   Sp Def   Speed   Generation   Legendary")
            for pokemon in new_deck_list:
                print(*pokemon)
    else:
        deck_completed = input("Please tell me if you would like a new deck. Just tell me yes or no")
    deck_completed = input("Do you like your new deck? Yes or No?")
    deck_completed = fix_string_input(deck_completed)
if deck_completed == "Yes":
    print("Awesome! Don't forget to add trainer cards and energy cards to your deck. Thank you for using the Pokemon Deck Creator! ")
