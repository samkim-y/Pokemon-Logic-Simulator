from time import sleep 
import random
from functions import GVI
from pokemon import Pokemon 

#Trainer Class
class Trainer:
    def __init__(self, name, party=None, bag=None):
        self.name = name
        self.party = [] 
        self.bag = [] 
        self.pokedex = []

    def add_to_pokedex(self,pokemon):
        if pokemon.dex_no not in self.pokedex: #add 
            self.pokedex.append(pokemon)
        else: #don't add 
            pass 

    def check_pokedex(self): #need to edit
        pass

    def add_pokemon (self, pokemon):
        if len(self.party)<6:
            self.party.append(pokemon)
        else: 
            print("There are too many Pokemon in your party!")

    def add_to_bag(self,item):
        self.bag.append(item)
    
    def remove_from_bag(self,item):
        self.bag.remove(item)

    def view_pokemon_party(self):
        if not self.party:
            print("Your party is empty!")
        else:
            print(f"{self.name}'s Pokémon Party:")
            for poke in self.party:
                print(f"- {poke.name}")
    
    def view_bag(self):
        if not self.bag:
            print("\nBag is empty!")
        else:
            print(f"{self.name}'s Bag:")
            for item in self.bag:
                print(f"- {item}")

    def remove_pokemon(self, pokemon):
        if pokemon in self.party:
            self.party.remove(pokemon)
            print(f"{pokemon.name} has been removed from your party!")
        else:
            print(f"{pokemon.name} is not in your party!")

    def choose_new_pokemon(self): #used when pokemon faints, and switch occurs (no Back option)
        while True:
            print("\nSelect a Pokemon:")
            letter_options = []
            for i,poke in enumerate(self.party):
                letter = chr(65+i)
                letter_options.append(letter)
                print(f"{letter}. {poke.name}")
            #choose pokemon 
            choose_pokemon = GVI("",letter_options)
            selected_pokemon = self.party[ord(choose_pokemon)-65]
            switch_or_check = GVI("\nA. Switch Pokemon\nB. Check Pokemon Stats\nC. Back\n",['A','B','C'])
            if switch_or_check == 'A': #switch pokemon 
                if selected_pokemon.status == 'Fainted':
                    print(f"\n{selected_pokemon.name} has already fainted!");sleep(0.5)
                else: 
                    return 'switch', selected_pokemon 
            elif switch_or_check == 'B': #check pokemon stats
                selected_pokemon.show_stats()
                sleep(0.5)
            else: #back 
                print(''); sleep(0.5)
    
    def battle_choice(self, pokemon, trainer_battle = 0): #main battle mechanics
        while True: 
            print(f"\nWhat will {pokemon.name} do?:")
            main_choice = GVI("A. Fight\nB. Pokemon\nC. Bag\nD. Run\n",['A','B','C','D'])
           
            #Fight Choice
            if main_choice == 'A': 
                while True:
                    print("\nSelect a move:")

                    #create move options based on available moves
                    letter_options = [] #store available options via letter (A - D)
                    for i, move in enumerate(pokemon.moves): #Generates A,B,C,D based on available moves (*using letters may not be most efficient, but created a good challenge)
                        letter = chr(65+i) #converts index to letter value
                        letter_options.append(letter) #stores available LETTERS 
                        print(f"{letter}. {move.name}") #print 'Letter. ' + Available Move  
                    #Add letter option for 'Back'
                    back_letter = (chr(ord(max(letter_options))+1)) #converts last letter generated above via ordinal, adds 1 and reconverts to letter 
                    print (f"{back_letter}. Back") 
                    letter_options.append(back_letter) #adding letter option for 'Back' to acceptable options list 
                   
                    #get player's move choice 
                    choose_move = GVI("",letter_options) 
                    if choose_move == back_letter: #player chooses Back: breaks back to main choice (fight, etc.)
                        break  
                    else: #player chooses a move 
                        selected_move = pokemon.moves[ord(choose_move)-65] #defines selected move by using index (converted from letter via ordinal value)

                        select_or_check = GVI("\nA. Select Move\nB. Check Move Stats\nC. Back\n",['A','B','C']) #get player option to select move or check move stats
                        if select_or_check == 'A': #Select Move: Returns specific move to Battle Function 
                            if selected_move.pp >0:
                                return 'fight', selected_move              
                            else:
                                print("\nThere's no PP left for this move!");sleep(0.5)
                        elif select_or_check == 'B': #Check Move Stats: prints Move stats, and returns to 
                            print(f"\n{selected_move.name }    PP:{selected_move.pp}/{selected_move.max_pp}\nType: {selected_move.type}\nCategory: {selected_move.category}\nPower: {selected_move.power}\nAccuracy: {selected_move.accuracy}%")
                            sleep(0.5)
                        else: #back
                            continue
            #Pokemon Choice
            elif main_choice == 'B': 
                while True:
                    print("\nSelect a Pokemon:")
                    letter_options = []
                    for i,poke in enumerate(self.party):
                        letter = chr(65+i)
                        letter_options.append(letter)
                        print(f"{letter}. {poke.name}")
                    back_letter = (chr(ord(max(letter_options))+1))
                    print (f"{back_letter}. Back") 
                    letter_options.append(back_letter) #adding letter option for 'Back' to acceptable options list 
                    #choose pokemon 
                    choose_pokemon = GVI("",letter_options)
                    if choose_pokemon == back_letter: #back to main option
                        break
                    else: #player chooses pokemon 
                        selected_pokemon = self.party[ord(choose_pokemon)-65]
                        switch_or_check = GVI("\nA. Switch Pokemon\nB. Check Pokemon Stats\nC. Back\n",['A','B','C'])
                        if switch_or_check == 'A': #switch pokemon 
                            if selected_pokemon.status == 'Fainted':
                                print(f"\n{selected_pokemon.name} has already fainted!");sleep(0.5)
                            elif selected_pokemon == pokemon:
                                print(f"\n{selected_pokemon.name} is already in battle!");sleep(0.5)
                            else: 
                                return 'switch', selected_pokemon 
                        elif switch_or_check == 'B': #check pokemon stats
                            selected_pokemon.show_stats()
                            sleep(0.5)
                        else: #back 
                            print(''); sleep(0.5)

            #Item Choice
            elif main_choice == 'C':
                if len(self.bag)>0: 
                    while True: 
                        print("\nSelect an item:")
                        letter_options = []
                        for i,item in enumerate(self.bag):
                            letter = chr(65+i)
                            letter_options.append(letter)
                            print(f"{letter}. {item.name}")
                        back_letter = (chr(ord(max(letter_options))+1))
                        print (f"{back_letter}. Back") 
                        letter_options.append(back_letter) #adding letter option for 'Back' to acceptable options list 
                        choose_item = GVI("",letter_options) #choose item 
                        if choose_item == back_letter:
                            break
                        else: #player chooses item 
                            selected_item = self.bag[ord(choose_item)-65]
                            use_or_check_effect = GVI("\nA. Use Item\nB. Check Effect\nC. Back\n",['A','B','C'])
                            if use_or_check_effect == 'A': #choose pokemon to use item on 
                                print("\nChoose which Pokemon to use the item on:")
                                poke_options = []
                                for i,poke in enumerate(self.party):
                                    poke_letter = chr(65+i)
                                    poke_options.append(poke_letter)
                                    print(f"{poke_letter}. {poke.name}")
                                poke_back_letter = (chr(ord(max(poke_options))+1))
                                print (f"{poke_back_letter}. Back") 
                                poke_options.append(poke_back_letter) #adding letter option for 'Back' to acceptable options list 
                                choose_pokemon = GVI("",poke_options)
                                if choose_pokemon == poke_back_letter: 
                                    continue
                                else: #pokemon is selected
                                    selected_pokemon = self.party[ord(choose_pokemon)-65]
                                    return 'item', [selected_item,selected_pokemon] #return item, 
                            elif use_or_check_effect == 'B': #too simple, needs to be edited (if item has no effect, etc.)
                                print('')
                                print(f"{selected_item.name}: {selected_item.effect}");sleep(0.8)
                else: 
                    print("\nYour bag is empty!");sleep(0.8)

            #Run Away 
            else:
                return 'run', None #need to edit? 

    def switch_pokemon(self,party,current_pokemon,is_player = True): #switches to new pokemon if current faints
        if any(pokemon.is_alive() for pokemon in party):
            print(f'\n{current_pokemon.name} has fainted!');sleep(0.6)
            print(f'\n{self.name}: You did well {current_pokemon.name}...');sleep(0.6)
            if is_player: 
                action, new_pokemon = self.choose_new_pokemon()
                current_pokemon = new_pokemon 
            else: #if opponent , automated switch to next pokemon in party 
                current_pokemon = party[1]#assigns next pokemon as current
                party.append(party.pop(0)) #moves fainted pokemon to end of party 
                print(f'...{self.name} sends out {current_pokemon.name}!');sleep(0.5)
                 
            print(f'\n{self.name}: Go, {current_pokemon.name}!');sleep(0.6) #leaves if statement (return current_pokemon)
        else: #no pokemon remaining in party 
            print(f'\n{current_pokemon.name} has fainted!');sleep(0.6)
            print(f'{self.name} is out of usable Pokemon!');sleep(0.6)
            return False
        return current_pokemon 

    
    def handle_attack_result(self, current_pokemon, opponent_pokemon,opponent, move, is_player =True): #returns true if battle continues/loops 
        if current_pokemon.perform_attack(opponent_pokemon,move): #if attack is successful 
            if opponent_pokemon.status =='Fainted': #if pokemon fainted
                if is_player: 
                    opponent_pokemon = opponent.switch_pokemon(opponent.party, opponent_pokemon, False) #if no availale pokemon, return is False, end battle; else, return switched pokemon 
                    return opponent_pokemon 
                else: 
                    opponent_pokemon = opponent.switch_pokemon(opponent.party, opponent_pokemon)
                    return opponent_pokemon 
            else: #pokemon has not fainted ; continues (True)
                return True 
        else: #attack misses , continues (True)
            return True 
        

    def battle(self, opponent, is_trainer = True):
        current_pokemon = self.party[0]#automatically chooses the first party member 

        if is_trainer: #trainer battle
            print(f"\n{opponent.name} has challenged {self.name}!\n");sleep(0.8)
            opponent_pokemon = opponent.party[0]#does same for opponent
            print(f'{opponent.name}: Go! {opponent_pokemon.species}!');sleep(0.6)            
        else: #wild pokemon
            print(f'\nA wild {opponent.name} Appears!')
            opponent_pokemon = opponent 
            
        print(f'{self.name}: Go! {current_pokemon.name}!');sleep(0.6)
  
        while True:
            action, action_input = self.battle_choice(current_pokemon) 
            opponent_attack = random.choice(opponent_pokemon.moves) #assign opponent attack to randomizer

            n = 1 # number of escape attempts
            #FIGHT
            if action =='fight': #action_input = selected_move
                n=1 #resets n to 1, if it wasn't already 
                
                if is_trainer: #Trainer battle 
                    if current_pokemon.speed >= opponent_pokemon.speed: #simplified turn priority mechanic (based on speed); YOU attack first 

                        player_turn = self.handle_attack_result(current_pokemon,opponent_pokemon,opponent, action_input)
                        if player_turn ==True:  #you attack and opponent is still alive , next they attack
                            opponent_turn = opponent.handle_attack_result(opponent_pokemon,current_pokemon, self, opponent_attack,False)
                            if opponent_turn== True:  #opponent attacked but you're still alive; turn ends (loop)
                                sleep(0.6) 
                                print(current_pokemon.is_alive())

                            elif opponent_turn == False: #you have no more pokemon, you lose (end)
                                print('');sleep(1)
                                break
                            else: #your pokemon fainted, but you switched pokemon; turn ends(loop)
                                current_pokemon = opponent_turn 
                        elif player_turn==False: #opponent has no more pokemon, oppenent loses (end)
                            print('');sleep(1)
                            break
                        else: 
                            opponent_pokemon = player_turn #opponent's pokemon fainted, but switched; turn ends (loop)

                    else: #OPPONENT attacks first 
                        opponent_turn = opponent.handle_attack_result(opponent_pokemon,current_pokemon, self, opponent_attack,False)
                        if opponent_turn ==True: 
                            player_turn = self.handle_attack_result(current_pokemon,opponent_pokemon,opponent, action_input)
                            if player_turn ==True:
                                sleep(0.6)
                            elif player_turn ==False:
                                print('');sleep(1)
                                break
                            else:
                                opponent_pokemon = player_turn
                        elif opponent_turn == False:
                            print('');sleep(1)
                            break
                        else:
                            current_pokemon = opponent_turn 

                else: #VS wild pokemon    
                    if current_pokemon.speed>= opponent_pokemon.speed: #you attack first
                        current_pokemon.perform_attack(opponent_pokemon,action_input) #attack 
                        if opponent_pokemon.is_alive(): #if opponent survives
                            opponent_turn = opponent_pokemon.wild_pokemon_attack(current_pokemon,self,opponent_attack)
                            if opponent_turn == False:
                                break #you lose, end battle 
                            elif opponent_turn == True: 
                                continue #no pokemon dies, loop 
                            else:
                                current_pokemon = opponent_turn #your pokemon dies, sent new pokemon , loop 
                        else: 
                            break #wild pokemon dies, end battle 
                    else: #wild pokemon attacks first
                        opponent_turn = opponent_pokemon.wild_pokemon_attack(current_pokemon,self,opponent_attack)
                        if opponent_turn ==False: 
                            break 
                        elif opponent_turn == True:
                            current_pokemon.perform_attack(opponent_pokemon,action_input)
                            if opponent_pokemon.is_alive():
                                continue
                            else: 
                                break 
                        else: 
                            current_pokemon = opponent_turn

            #Switch Pokemon 
            if action == 'switch': #action_input = new pokemon
                print(f'\nCome back, {current_pokemon.name}!');sleep(0.8)
                current_pokemon = action_input
                print(f'Go, {current_pokemon.name}!');sleep(0.8)
                if is_trainer: #Trainer battle 
                    opponent_turn = opponent.handle_attack_result(opponent_pokemon,current_pokemon, self, opponent_attack,False)
                    if opponent_turn== True:  #opponent attacked but you're still alive; turn ends (loop)
                        sleep(0.6) 
                    elif opponent_turn == False: #you have no more pokemon, you lose (end)
                        sleep(1)
                    else: #your pokemon fainted, but you switched pokemon; turn ends(loop)
                        current_pokemon = opponent_turn 
                else: #VS wild pokemon 
                    if opponent_pokemon.wild_pokemon_attack(current_pokemon,self,opponent_attack)==False:
                        break
                    else: 
                        continue 

            #Use Item 
            if action =='item':
                if action_input[0].perform_action(action_input[1],self):
                    if is_trainer:
                        opponent_turn = opponent.handle_attack_result(opponent_pokemon,current_pokemon, self, opponent_attack,False)
                        if opponent_turn== True:  #opponent attacked but you're still alive; turn ends (loop)
                            print('');sleep(1) 
                        elif opponent_turn == False: #you have no more pokemon, you lose (end)
                            print('');sleep(1)
                        else: #your pokemon fainted, but you switched pokemon; turn ends(loop)
                            current_pokemon = opponent_turn 
                    else: 
                        if opponent_pokemon.wild_pokemon_attack(current_pokemon,self,opponent_attack)==False:
                            break
                        else: 
                            continue 
                        

            #Run 
            if action =='run':
                if is_trainer:
                    print("\nYou can't run from a Trainer Battle!");sleep(1)
                else: 
                    odds = ((current_pokemon.speed*32)/((opponent.speed)/4)%256)+30*n 
                    if odds > 255: #player automatically escapes
                        print('\nyou escape')#****
                    else: 
                        if random.randint(0,256)<odds:
                            print('you escape');sleep(1)
                            return True #end battle 
                        else: 
                            print('\nYou couldnt escape');sleep(1) #failed to escape
                            n+=1 #adds escape attempts 


        #end of battle 
        if is_trainer:
            if any(pokemon.is_alive() for pokemon in self.party): 
                print(f'{self.name} has defeated {opponent.name}!') #no money in this game
                return True
            else: 
                print(f'{opponent.name} has defeated {self.name}!') #what do we do after player is defeated? ********
                return False
        else: #wild pokemon battle
            if any(pokemon.is_alive() for pokemon in self.party): #you win/wild pokemon fainted
                print(f'\nThe wild {opponent.name} fainted!')
                return True 
            else: #all your pokemon fainted, you black out
                print(f'{self.name} blacked out');sleep(1)
                return False 


