from time import sleep
import random 


class Pokemon: 
    def __init__(self,dex_no, species, max_hp, attack, defense,sp_atk, sp_def,speed, moves, level, base_exp, owned, exp, type1, type2=None, status ='Active'): #add pokedex no. 
        self.dex_no = dex_no 
        self.name = species #default set same as species 
        self.species = species 
        self.level = level
        self.hp = max_hp #current hp of pokemon ()
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed 
        self.moves = moves
        self.level = level
        self.base_exp = base_exp
        self.owned = owned #1.5 if owned, 1 if wild
        self.exp = exp 
        self.type1 = type1
        self.type2 = type2 
        self.status = status 

    def restore(self):
        self.hp = self.max_hp
        self.status = 'Active'

    def is_alive(self):
        return self.hp>0
    
    def take_damage(self,damage): #t
        self.hp -=damage 
        if self.hp<=0:
            self.hp = 0 
            self.status = 'Fainted'
            print(f'{self.name} has taken {damage} damage!');sleep(0.8)
        else: 
            print(f'{self.name} has taken {damage} damage! HP is down to {self.hp}/{self.max_hp}');sleep(0.4)

    def damage(self, move, defender):
        crit_rand = random.randint(0,255) #critical definition 
        crit_threshold = min((self.speed+76)/4 ,255)
        
        if crit_rand < crit_threshold:
            critical = (2*self.level+5)/(self.level+5)
            print('A critical hit!');sleep(0.5)
        else: 
            critical = 1 

        if move.category == 'Physical': #AD_ratio definition
            AD_ratio = self.attack/self.defense 
        elif move.category =='Special':
            AD_ratio = self.sp_atk/self.sp_def 

        if move.type == self.type1 or move.type == self.type2: #STAB definition
            STAB = 1.5 
        else: 
            STAB = 1 

        type1 = self.type_effectiveness(move.type, defender.type1)
        type2 = self.type_effectiveness(move.type,defender.type2)
        random_factor = random.uniform(0.85,1)

        if type1 == 2 or type2 == 2: 
            print("It's super effecive!");sleep(0.5)
        elif type1 ==0.5 or type2 ==0.5:
            print("It wasn't very effective..."); sleep(0.5)
        #main damage equation
        damage = ((((((2*self.level*critical)/5)+2)* move.power* AD_ratio)/50)+2)*STAB * type1 * type2 *random_factor

        return max(0, int(damage))

    def perform_attack(self, defender, move): #handles attack logic for attacker using given move
        move.pp -=1
        if random.randint(1,100) <= move.accuracy:
            print(f'\n{self.name} used {move.name}!');sleep(0.6)            
            defender.take_damage(self.damage(move,defender))
            return True  #attack succeeded 
        else:
            print(f'\n{self.name} tried to use {move.name}!');sleep(0.6)
            print(f'but {self.name} missed!');sleep(0.6)
            return False 
    
    def wild_pokemon_attack(self,defender_pokemon, defender, move,is_player=True):
        if self.perform_attack(defender_pokemon, move): #opponent attack lands
            if defender_pokemon.is_alive(): 
                sleep(0.5) #loop continues 
            else: #your pokemon fainted 
                return defender.switch_pokemon(defender.party, defender_pokemon) #returns False or new pokemon 
        return True #continue loop (whether miss or not)
    
    def type_effectiveness(self, move_type, defender_type): #may need editing
        """
        Simple type effectiveness chart.
        Returns multiplier based on attacker's move type and defender's Pokémon type.
        """
        type_chart = {
            'Normal': {'Normal':1, 'Fire':1, 'Water':1, 'Electric':1, 'Grass':1, 'Ice':1, 'Fighting':1, 'Poison':1, 'Ground':1, 'Flying':1, 'Psychic':1, 'Bug':1,'Rock':0.5 ,'Ghost':0, 'Dragon':1},
            'Fire': {'Normal':1, 'Fire':0.5, 'Water':0.5, 'Electric':1, 'Grass':2, 'Ice':2, 'Fighting':1, 'Poison':1, 'Ground':1, 'Flying':1, 'Psychic':1, 'Bug':2,'Rock':0.5 ,'Ghost':1, 'Dragon':0.5},
            'Water': {'Normal':1, 'Fire':2, 'Water':0.5, 'Electric':1, 'Grass':0.5, 'Ice':1, 'Fighting':1, 'Poison':1, 'Ground':2, 'Flying':1, 'Psychic':1, 'Bug':1,'Rock':2 ,'Ghost':1, 'Dragon':0.5},
            'Electric': {'Normal':1, 'Fire':1, 'Water':2, 'Electric':0.5, 'Grass':0.5, 'Ice':1, 'Fighting':1, 'Poison':1, 'Ground':0, 'Flying':2, 'Psychic':1, 'Bug':1,'Rock':1 ,'Ghost':1, 'Dragon':0.5},
            'Grass': {'Normal':1, 'Fire':0.5, 'Water':2, 'Electric':1, 'Grass':0.5, 'Ice':1, 'Fighting':1, 'Poison':0.5, 'Ground':2, 'Flying':0.5, 'Psychic':1, 'Bug':0.5,'Rock':2 ,'Ghost':1, 'Dragon':0.5},
            'Ice': {'Normal':1, 'Fire':1, 'Water':0.5, 'Electric':1, 'Grass':2, 'Ice':0.5, 'Fighting':1, 'Poison':1, 'Ground':2, 'Flying':2, 'Psychic':1, 'Bug':1,'Rock':1 ,'Ghost':1, 'Dragon':2},
            'Fighting': {'Normal':2, 'Fire':1, 'Water':1, 'Electric':1, 'Grass':1, 'Ice':2, 'Fighting':1, 'Poison':0.5, 'Ground':1, 'Flying':0.5, 'Psychic':0.5, 'Bug':0.5,'Rock':2 ,'Ghost':0, 'Dragon':1},
            'Poison': {'Normal':1, 'Fire':1, 'Water':1, 'Electric':1, 'Grass':2, 'Ice':1, 'Fighting':1, 'Poison':0.5, 'Ground':0.5, 'Flying':1, 'Psychic':1, 'Bug':2,'Rock':0.5 ,'Ghost':0.5, 'Dragon':1},
            'Ground': {'Normal':1, 'Fire':2, 'Water':1, 'Electric':2, 'Grass':0.5, 'Ice':1, 'Fighting':1, 'Poison':2, 'Ground':1, 'Flying':0, 'Psychic':1, 'Bug':0.5,'Rock':2 ,'Ghost':1, 'Dragon':1},
            'Flying': {'Normal':1, 'Fire':1, 'Water':1, 'Electric':0.5, 'Grass':2, 'Ice':1, 'Fighting':2, 'Poison':1, 'Ground':1, 'Flying':1, 'Psychic':1, 'Bug':2,'Rock':0.5 ,'Ghost':1, 'Dragon':1},
            'Psychic': {'Normal':1, 'Fire':1, 'Water':1, 'Electric':1, 'Grass':1, 'Ice':1, 'Fighting':2, 'Poison':2, 'Ground':1, 'Flying':1, 'Psychic':0.5, 'Bug':1,'Rock':1 ,'Ghost':1, 'Dragon':1},
            'Bug': {'Normal':1, 'Fire':0.5, 'Water':1, 'Electric':1, 'Grass':2, 'Ice':1, 'Fighting':0.5, 'Poison':2, 'Ground':1, 'Flying':0.5, 'Psychic':2, 'Bug':1,'Rock':1 ,'Ghost':0.5, 'Dragon':1},
            'Rock': {'Normal':1, 'Fire':2, 'Water':1, 'Electric':1, 'Grass':1, 'Ice':2, 'Fighting':0.5, 'Poison':1, 'Ground':0.5, 'Flying':2, 'Psychic':1, 'Bug':2,'Rock':1 ,'Ghost':1, 'Dragon':1},
            'Ghost':{'Normal':0, 'Fire':1, 'Water':1, 'Electric':1, 'Grass':1, 'Ice':1, 'Fighting':1, 'Poison':1, 'Ground':1, 'Flying':1, 'Psychic':0, 'Bug':1,'Rock':1 ,'Ghost':2, 'Dragon':1},
            'Dragon':{'Normal':1, 'Fire':1, 'Water':1, 'Electric':1, 'Grass':1, 'Ice':1, 'Fighting':1, 'Poison':1, 'Ground':1, 'Flying':1, 'Psychic':1, 'Bug':1,'Rock':1 ,'Ghost':1, 'Dragon':2}            
            }
        
        # Default multiplier is 1 (no effectiveness)
        return type_chart.get(move_type, {}).get(defender_type, 1) 

    def show_stats(self): #edit
        print("\n____________________")        
        if self.status != 'Active':
            print(f"{self.name} Lv.{self.level} ({self.status})\n{self.species} Dex No.{self.dex_no}\n\nHP: {self.hp}/{self.max_hp}\nATTACK: {self.attack}\nDEFENSE: {self.defense}\nSP. ATK: {self.sp_atk}\nSP. DEF: {self.sp_def}\nSPEED: {self.speed}\n")
        else: 
            print(f"\n{self.name} Lv.{self.level}\n{self.species} Dex No.{self.dex_no}\n\nHP: {self.hp}/{self.max_hp}\nATTACK: {self.attack}\nDEFENSE: {self.defense}\nSP. ATK: {self.sp_atk}\nSP. DEF: {self.sp_def}\nSPEED: {self.speed}\n")            
        print("<MOVES>")
        for move in self.moves:
              print(f"{move.name} [{move.type}] PP:{move.pp}/{move.max_pp}")
        print("____________________\n") 
        sleep(0.5)


    def exp_gain(pokemon1, pokemon2, s): #pokemon1 = victor; #pokemon2 = fainted ; s = number of pokemon participating in battle (not fainted)
        if pokemon2.owned == 1:
            a = 1.5 
        else: 
            a = 1 
        exp_gain = ((pokemon2.base_exp * pokemon2.level)/7) * (1/s) * a 
        pokemon1.exp += exp_gain



#Moves class
class Move: 
    def __init__(self, name, power, category, type, max_pp, accuracy = 100 , effect = 'none'):
        self.name = name
        self.power = power
        self.category = category 
        self.type = type 
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.pp = max_pp 
        self.effect = effect 

    def show_stats(self):
        print(f"\n{self.name}\nPower: {self.power}\nCategory: {self.category}\nType: {self.type}\n Accuracy: {self.accuracy}%\nPP: {self.pp}")

class Move: 
    def __init__(self, name, power, category, type, max_pp, accuracy = 100 , effect = 'none'):
        self.name = name
        self.power = power
        self.category = category 
        self.type = type 
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.pp = max_pp 
        self.effect = effect 

    def show_stats(self):
        print(f"\n{self.name}\nPower: {self.power}\nCategory: {self.category}\nType: {self.type}\n Accuracy: {self.accuracy}%\nPP: {self.pp}")
