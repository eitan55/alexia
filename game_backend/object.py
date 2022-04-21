#Pour définir les objets (pièces, équipement, monstre)

coin = 'C'
gun = 'G'
monster = 'M'

class Object:
    def __init__(self, pos_x, pos_y, map):
        self.x = pos_x
        self.y = pos_y
        self.map = map
    
    def erase(self): #j'ai pas forcément compris comment marche la fonction __del__, et j'ai lu qu'il fallait pas forcément l'utiliser
        #le nom delete est déjà une fonction numpy, si vous avez des meilleurs noms allez-y
        self.map[self.x][self.y] = 'x' #j'ai fait comme dans la classe player

class Money(Object):
    def __init__(self, pos_x, pos_y, map):
        super.__init__(pos_x, pos_y, map)
        self.map[self.x][self.y] = coin
    
    def erase(self, player): #je suppose que le score est défini à part, pour avoir le score total
        player.money_score += 1 #chaque pièce rapporte 1
        super().erase(self)

class Equipment(Object):
    def __init__(self, pos_x, pos_y, map, equipment = gun):
        super().__init__(pos_x, pos_y, map)
        self.equipment = equipment
        self.map[pos_x][pos_y] = self.equipment

    def erase(self, player):
        player.bag.append(self.equipment)
        super().erase(self)
    
    #la force du player peut varier en fonction de son équipement

class Monster(Object):
    def __init__(self, pos_x, pos_y, map, shown = True):
        super().__init__(pos_x, pos_y, map)
        if shown == True:
            self.map[self.x][self.y] = monster
        self.life = 1 #j'ai mis que le monstre avait une vie pour l'instant, on pourra le changer après
    
    def attack(self, player, way = 1):
        #pour l'instant :
        # way = 1 --> le joueur "attaque" le monstre
        # way = -1 --> le monstre attaque le joueur, qui perd une vie
        if way == 1:
            self.life -= 1
        elif way == -1:
            #j'ai changé le init de la la class player pour ajouter un nombre de vie au joueur
            player.lose_a_life() #!!! il faut changer la class player pour que le joueur meurt (ou rajouter ça quelque part dans le code)
        #il faut faire attention dans le reste du code que le monstre ne perde pas de vie sauf ici (ou changer le code ici)
        if self.life == 0:
            self.delete()
        #il faut mettre une fonction attack chez le player

    def erase(self):
        super().erase(self)