#tas_kagit_makas_EMRE_KOCABIYIKOGLU


import random
import time

print("As the adventurer steps into the grand hall of the wizard's castle, the air shimmers with ancient magic.\n"
      "The wizard, a quirky figure with a long, twisted beard and a robe embroidered with strange symbols, greets the adventurer with a mischievous grin.\n\n"
      "'Ah, a brave soul has wandered into my domain!' the wizard cackles, his eyes twinkling with playful energy.\n"
      "'But before you seek my wisdom or my treasure, we must play a game—a game of elements and wits! A game older than the stones beneath your feet!'\n\n"
      "The wizard swirls his hands in the air, conjuring a glowing circle of symbols representing the five elements: Fire, Earth, Metal, Water, and Wood.\n"
      "'This be no simple child's play like the commoner's Rock, Paper, Scissors! Nay, this be a game of power, where Fire devours Earth and boils Water! But beware, for Earth can crush Metal and sap the strength of Wood! Metal, with its cold resolve, conquers Fire and Water! Yet, Water quenches the flames and drowns Earth’s might! And finally, Wood, the humble bringer of life, feeds Fire and bends Metal to its will!'\n\n"
      "The wizard chuckles, clearly delighted by the thought of the upcoming contest.\n"
      "'Choose wisely, adventurer, for in this game of fates, even the smallest spark may ignite a victory, or a mighty mountain may fall to the simplest wave!'\n\n"
      "With a dramatic flourish, the wizard spreads his hands wide.\n"
      "'Shall we begin? May the elements favor the bold and the clever!'\n")


def tas_kagit_makas_EMRE_KOCABIYIKOGLU():
    # Define the elements 
    elements = ["metal", "wood", "earth", "fire", "water"]

    def determine_winner(player_choice, wizard_choice):
        if player_choice == wizard_choice:
            print("It's a tie!")
            return "tie"
        
        if player_choice == "fire":
            if wizard_choice == "earth":
                print("Fire devours Earth!")
                return "player"
            elif wizard_choice == "water":
                print("Fire boils Water!")
                return "player"
            else:
                print("Fire is defeated!")
                return "wizard"
        
        elif player_choice == "earth":
            if wizard_choice == "metal":
                print("Earth crushes Metal!")
                return "player"
            elif wizard_choice == "wood":
                print("Earth saps the strength of Wood!")
                return "player"
            else:
                print("Earth is defeated!")
                return "wizard"
        
        elif player_choice == "metal":
            if wizard_choice == "fire":
                print("Metal is melted by Fire!")
                return "wizard"
            elif wizard_choice == "water":
                print("Metal rusts in Water!")
                return "wizard"
            else:
                print("Metal prevails!")
                return "player"
        
        elif player_choice == "water":
            if wizard_choice == "wood":
                print("Water nourishes Wood!")
                return "player"
            elif wizard_choice == "earth":
                print("Water erodes Earth!")
                return "player"
            else:
                print("Water is defeated!")
                return "wizard"
        
        elif player_choice == "wood":
            if wizard_choice == "fire":
                print("Wood burns in Fire!")
                return "wizard"
            elif wizard_choice == "metal":
                print("Wood is bent by Metal!")
                return "wizard"
            else:
                print("Wood triumphs!")
                return "player"
        
        # Default return in case of invalid input 
        print("Invalid choices!")
        return "invalid"

    # game mechanism
    def play_game(game_number):
        player_score = 0
        wizard_score = 0
        round_number = 1

        while player_score < 2 and wizard_score < 2:
            print(f"******* GAME {game_number} ROUND {round_number} *******")
            choice = input("Choose Metal, Wood, Earth, Fire, Water or Exit: ").strip().lower()

            if choice in elements:
                wizard_choice = random.choice(elements)
                print(f"You chose {choice.capitalize()}!")
                print(f"The wizard chose {wizard_choice.capitalize()}!")

                result = determine_winner(choice, wizard_choice)
                
                if result == "player":
                    player_score += 1
                    print("You win this round!")
                elif result == "wizard":
                    wizard_score += 1
                    print("The wizard wins this round!")

                print(f"Score - Adventurer: {player_score}, Wizard: {wizard_score}")
                round_number += 1  
                
                # Move to the next round
                
                time.sleep(1)
                

                # Add a  gap  between rounds
               
                print("\n" * 2)
            elif choice == "exit":
                print("Exiting the game. Farewell, adventurer!")
                return False  
                # Exit the game
            else:
                print("Invalid choice! Please choose again.","\n" * 2)

        if player_score == 2:
            print("Congratulations! You won the game!")
        else:
            print("The wizard won the game. Better luck next time!")

        return True  # Indicate that the game ended and the player can play again

    

    

    game_number = 1

    while True:
        if not play_game(game_number):
            break

        # Ask the player if they want to play another game
        player_wants = input("Do you want to play another game? (yes/no): ").strip().lower()
        
        # Decide if the wizard wants to play another game
        wizard_wants = random.choice([True, False])
        
        if player_wants == "yes" and wizard_wants:
            game_number += 1
            print(f"******* GAME {game_number} ROUND 1 *******")
        elif player_wants == "yes" and not wizard_wants:
            print("The wizard has decided not to play another game. Farewell!")
            break
        else:
            print("Farewell, adventurer!")
            break

# Call the function to start the game
tas_kagit_makas_EMRE_KOCABIYIKOGLU()
