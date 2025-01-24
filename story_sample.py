from time import sleep
import random
import copy 
from trainer import Trainer 
from functions import GVI
from pokemon import *
from items import Item
from pokemon_model import *
#finalize pokemon attributes
#add EXP system 
#add leveling system
#add pokedex 
#add remaining pokemon

#complete story
#add stores + pokemon center 


#Items
super_potion = Item('Super Potion','medical','Adds 100HP to the chosen Pokemon')
potion = Item('Potion','medical','Adds 50 HP to chosen Pokemon')







#pregame (ask gender, name)
def scene_0():
    global player
    print("Hello! Welcome to the World of Pokemon!");sleep(0.8)
    print("My name is Professor Oak\n");sleep(0.8)
    
    print("First, what are you a boy or a girl?");sleep(0.8)
    gender = GVI("A. Boy\nB. Girl\nC. I don't know\n", ['A','B','C'])

    print("\nI see...");sleep(0.8)
    if gender == 'A' or gender =='B':    
        print("I wasn't really sure. but I see...\n");sleep(1)
    else: 
        print("You don't even know...");sleep(1)
        print("...");sleep(0.8)
        print("Let's move on...\n");sleep(0.8)

    name = input("Alright, what's your name?\n");sleep(0.8) #name input 
    print("")
    print (name+"?")#sleep(0.8)
    print("What a weird name...");sleep(1.5)
    print("Well. Who am I do judge...\n");sleep(0.8)

    print("Anyways, let's begin your journey");sleep(0.8)
    print("Welcome to the world of Pokemon!\n");sleep(1)
    player = Trainer(name)
    choose_first_pokemon()

    '''
    scene_1()

def scene_1():
   
    print("...You recently moved to Pallet Town...");sleep(1.5)
    print("...")#;sleep(0.8)
    print("Mom: "+player.name+"!" );sleep(0.8)
    print("Mom: Come downstairs!")

    print("... skipping some story... still in progress... ")
    choose_first_pokemon()
    '''


def choose_first_pokemon():
    global player_pokemon1
    while True: 
        pick_pokemon = GVI("Pick a pokemon:\nA. Charmander\nB. Bulbasaur\nC. Squirtle\n",['A','B','C'])
        if pick_pokemon == 'A':
            pick_pokemon = charmander 
        elif pick_pokemon == 'B':
            pick_pokemon = bulbasaur
        else:
            pick_pokemon = squirtle 

        pick_choice = GVI("\nDo you want to:\nA. Choose Pokemon\nB. Show Stats\nC. Back\n",['A','B','C'])
        if pick_choice == 'A': #pick pokemon 
            first_pokemon = pick_pokemon
            sleep(0.8)
            break
            
        elif pick_choice == 'B': #show stats
            pick_pokemon.show_stats();sleep(0.8)
            pick_choice = GVI("\nDo you want to pick this pokemon? (Y/N):",['Y','N'])
            if pick_choice == 'Y':
                first_pokemon = pick_pokemon 
                sleep(0.5)
                break
            else: 
                print("");sleep(0.8)

        else: #back 
            print("");sleep(0.8)

    print("\nYou have chosen "+first_pokemon.name+ " as your first pokemon!\n");sleep(0.5)
    player_pokemon1 = copy.deepcopy(first_pokemon)

    while True:  
        give_name = GVI(f"Would you like to give a nickname to {player_pokemon1.name}? (Y/N): ", ['Y','N'])
        if give_name == 'N':
            sleep(1.5)
            break
        else: #give nickname 
            pokemon1_nickname = input(f"\n{player_pokemon1.name}'s nickname?: ");sleep(0.5)
            confirm_nickname = GVI(f'Do you want to nickname {player_pokemon1.name} as {pokemon1_nickname}? (Y/N): ',['Y','N'])
            if confirm_nickname == 'Y':
                player_pokemon1.name = pokemon1_nickname 
                sleep(1.5)
                break
            else: 
                print('')
                sleep(0.4)        
    player.add_pokemon(player_pokemon1)
    first_battle(first_pokemon)
        
def first_battle(first_pokemon): #introduction of rival                
    print("\nUnknown: ...WAIT!\n");sleep(0.8)
    print("...suddenly someone bursts into the lab...\n");sleep(0.8)
    print("Unknown: Hey you!");sleep(0.8)
    print("Unknown: Theres only one person worthy of being a master Pokemon Trainer around here!\n");sleep(1)

    print("Professor Oak: ...");sleep(0.8)
    print("Professor Oak: Oh, I'm sorry");sleep(0.8)
    print("Professor Oak: This is my grandson, I believe you know him");sleep(0.8)
    print("Professor Oak: ...");sleep(0.8)
    print("Professor Oak: What was his name again...?"); sleep(0.8)
    print("Professor Oak: Do you remember?\n");sleep(0.8)
    rival_name = input("What is your rival's name:\n")
    rival = Trainer(rival_name)

    print("\nProfessor Oak: Ah, that's right!");sleep(0.8)
    print("Professor Oak: His name is "+rival.name+"\n");sleep(1)

    print(rival.name +": ...");sleep(1)
    print(rival.name +": Grandpa...");sleep(1)
    print(rival.name +": How can you forget my name...\n");sleep(1)
    print("...Everyone stands in awkward silence as you hear soft sniffling...\n"); sleep(1.5)
    print(rival.name +": Anyways... That's right!");sleep(0.8)
    print(rival.name +": We've been rivals since we were young remember?!?");sleep(0.8)
    print(rival.name +": Before I moved away and came to this town 8 years ago!");sleep(1.5)
    print(rival.name +": ...");sleep(1)
    print(rival.name +": Why are you just staring at me like that..");sleep(1)
    print(rival.name +": Don't tell me you forgot... \n");sleep(1)
    print(rival.name+ ": ...");sleep(1)
    print(rival.name +": Well... that'll be your downfall. You never saw me coming!");sleep(0.8)
    print(rival.name +": You chose "+first_pokemon.name +", huh?");sleep(0.8)
    if first_pokemon == charmander:
        rival_pokemon = squirtle
    elif first_pokemon == bulbasaur:
        rival_pokemon = charmander
    else:
        rival_pokemon = bulbasaur

    rival_pokemon1 = copy.deepcopy(rival_pokemon) #creates new object of rival pokemon 
    rival_pokemon1.name = f"{rival.name}'s {rival_pokemon.name}"
    rival.add_pokemon(rival_pokemon1)
    print(rival.name +": Then I'll choose "+rival_pokemon.name+"!");sleep(0.8)
    while True: 
        if player.battle(rival):
            sleep(1)
            break
        else:
            print(f"\n{rival.name}: That's all you got, huh?");sleep(0.5)
            print(f"{rival.name}: Well come on, let's give it another go");sleep(0.5)
            player_pokemon1.restore()
            rival_pokemon1.restore()

    print(f"\n{rival.name}: ...");sleep(1)
    print(f"{rival.name}: That's not fair!");sleep(0.5)
    print(f"{rival.name}: You cheated!");sleep(0.5)
    print(f"{rival.name}: ...");sleep(1.5)
    print(f"{rival.name}: That won't be the last you see of me!\n");sleep(0.5)
    
    print(f'...{rival.name} runs away...\n');sleep(1)

    print("Professor Oak: Well..");sleep(0.5)
    print("Professor Oak: That sure was weird");sleep(0.5)

    

    





scene_0()
