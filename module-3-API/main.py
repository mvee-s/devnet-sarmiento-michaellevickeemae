# Randomly select one pokemon from a list


# Display height and weight without reveal
#get
# 3 Attempts to guess the pokemon
#limit
# Winning message for correct guess
#Reveal the correct if failes
#handle invalid names and network errors

import requests
response = requests.get("https://pokeapi.co/")

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print("Failed to fetch.")

def get_pokemon(number):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print("Pokemon not found.")

def display_pokemon(data):

    if data:
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")

    else:
        print("Pokemon not found.")

def main():
    pokemon_number = int(input("Select a number: "))
    pokemon_data = get_pokemon(pokemon_number)
    display_pokemon(pokemon_data)

main()
