import random

def open_file(name, mode):# opens csv file
    fileobj = open(name, mode)
    return fileobj


def load_raw_data(fileobj):# reads the csv file
    return fileobj.readlines()


def parse_raw_data(raw_data_list):# seperates each item in a list by a comma
    plist = []
    for data_item in raw_data_list:
        x = data_item.split(",")
        plist.append(x)
    return plist

def PoketypesA(typeA, list):
    found = -1
    for i in range(0, len(list)):
        x = list[i].lower().find(typeA.lower())
        if x >= 0:
            found = i
            break
    return found


def parse_pokemon_data(index_data):  # this function pulls the third object (pokemon types) out of each list.
    pokemon_types_list = []
    for pokemon in index_data:
        temp_pokemon_type = pokemon[2]
        if temp_pokemon_type not in pokemon_types_list: # keeps the list from having duplicates
            pokemon_types_list.append(temp_pokemon_type)
    return pokemon_types_list


def fix_string_input(answer):
    answer = answer.strip().lower().capitalize() # takes away white space, puts the whole input in lower case, and capitalizes the first letter
    return answer


def remove_brackets(type_list):
    type_list = " ".join(map(str, type_list))
    return type_list

def pokemon_with_common_types(indexed, deck_type):
    similar_pokemon_list = []
    for pokemon in indexed:
        if pokemon[2] in deck_type: # checks position two in the indexed data and compares it to what the user asked for
            similar_pokemon_list.append(pokemon)
        if pokemon[3] in deck_type:# same as line 52 but checks the TypeB column indexed data or position 3
            similar_pokemon_list.append(pokemon)
    return similar_pokemon_list


def randomize(pokemon_list):
    deck_list = []
    while len(deck_list) < 20:
        random_number = random.randint(0, len(pokemon_list)-1) #choses random
        pokemon = pokemon_list[random_number] #sets pokemon to name that corresponds with random number chosen
        deck_list.append(pokemon)
    return deck_list