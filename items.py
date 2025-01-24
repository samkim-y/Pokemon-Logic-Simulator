from time import sleep 
from pokemon import Pokemon 
from trainer import Trainer


#Item Class
class Item: 
    def __init__(self, name, category, effect):
        self.name = name
        self.category = category
        self.effect = effect 

    def perform_action(self,pokemon,trainer):
        if self.category == 'medical':
            return self.medical(pokemon,trainer)
        
    def medical(self,pokemon,trainer):
        if pokemon.hp < pokemon.max_hp:
            if self.name =='Potion':
                pokemon.hp+=50             
            elif self.name =='Super Potion':
                pokemon.hp +=100 
            
            if pokemon.hp > pokemon.max_hp: #limit hp to max_hp
                pokemon.hp = pokemon.max_hp

            trainer.remove_from_bag(self)
            print(f"\nUsed {self.name} on {pokemon.name}");sleep(0.6)
            print(f"{pokemon.name}'s HP is now {pokemon.hp}/{pokemon.max_hp}");sleep(1)    
            return True  

        else: #item used
            print(f"\n{pokemon.name}'s HP is already full!");sleep(1)
            return False