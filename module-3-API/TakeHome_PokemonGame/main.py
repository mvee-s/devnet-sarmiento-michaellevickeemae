import random
import requests

pokemon_URL = "https://pokeapi.co/api/v2/pokemon/"

pokemon_names = [
    "pikachu",
    "bulbasaur",
    "ninetales",
    "psyduck",
    "gengar",
    "snorlax",
    "eevee"

]

def get_pokemon(name):
    response = requests.get(pokemon_URL + name, timeout=10)

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 404:
        return None

    else:
        response.raise_for_status()

def display_clues(data):
       
        height = data["height"]
        weight = data["weight"]

        print("Height: ", height)
        print("Weight: ", weight)
        print("Abilities: ")
        
        for item in data["abilities"]:
            ability = item["ability"]["name"]
            print("-", ability)

def guessing_game(name, data):
    print("\n===== Guess Who is this! =====")
    display_clues(data)

    for attempt in range(1,4):
        guess = input(f"\nAttempt {attempt}/3. \nEnter Pokemon name: ").lower().strip()

        try:
            if guess == "":
                print("You entered a blank answer. Still counts as attempt. Kindly enter a correct Pokemon name.")
                continue

            guessed_data = get_pokemon(guess)

            if guessed_data is None:
                print("\nUh Oh! Invalid Pokemon Name :(")
              
            elif guess ==  name:
                print("\nYay! Congratulations! You guessed it correctly!")
                return
                                  
            else:
                print("\nEnk! Wrong Guess! Try again.")
        
        except requests.exceptions.RequestException:
            print("Network error! Please check your internet connection.")
            return
        
    print(f"\nGame Over! The pokemon was {name.title()}.")   

def main(): 
    
        print("\n===== GUESS YOUR POKEMON GAME =====")
        print("Mechanics: ")
        print("1. Analyze the clues then type your guess.")
        print("2. Think wisely! You only have 3 attempts.")

        user_decision = input("Start Game? (y/n): ").lower().strip()

        if user_decision == "n":
            print("\nThank you for playing!")
            return

        elif user_decision != "y":
            print("\nInvalid choice. Please enter y or n only.")
            return

        while True:
            try:
                answer = random.choice(pokemon_names)
                data = get_pokemon(answer)


                if data is not None:
                    guessing_game(answer, data)

                else:
                    print("\nUnable to retrieve Pokemon data.")
                    break

            except requests.RequestException:
                print("\nNetwork error! Please check your internet connection.")
                break
            
            play_again = input("\nDo you want to play againn? (y/n): ").lower().strip()

            if play_again == "y":
                print("\n====== NEW ROUND ======")
                print("Ready?")
                continue

            else:
                print("\nThank you for playing!")
                break

main()
    
