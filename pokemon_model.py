from pokemon import Pokemon,Move

#moves
scratch = Move("Scratch", 35, 'Physical', 'Normal',35)
ember = Move("Ember", 40, "Special", "Fire",25)
tackle = Move("Tackle",40, "Physical", "Normal", 35)
vine_whip = Move("Vine Whip",40, "Physical","Grass",25)
razor_leaf = Move("Razor Leaf",55, "Physical","Grass",25,95)
water_gun = Move("Water Gun",40,"Special","Water",25)
rapid_spin = Move("Rapid Spin",50, "Physical", "Normal",40)
punch_in_face = Move("Punch in the Face", 1000,"Physical","Normal",4,50)

#pokemon
charmander = Pokemon('04' ,"Charmander", 39, 52, 43, 60, 50, 65, [scratch, ember,punch_in_face, tackle],5, 62, 1,0,"Fire") #add other moves
bulbasaur = Pokemon('01',"Bulbasaur", 45, 49, 49, 65, 65, 45, [tackle,vine_whip, razor_leaf, scratch], 5, 64, 1,0,"Grass")#add leechseed 
squirtle = Pokemon('07',"Squirtle", 44, 48, 65, 50, 64, 43, [tackle, water_gun,rapid_spin, scratch ], 5, 63, 1,0, "Water") #add withdraw


class Charmander(Pokemon): 
    def __init__ (self,name): 
        self.name = name 


    
    