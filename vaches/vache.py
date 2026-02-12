import vaches.exceptions
from vaches.exceptions import InvalidVacheException

import vaches.TypeNourriture
from vaches.TypeNourriture import TypeNourriture

class Vache:
    
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN = 2.0
    RENDEMENT_RUMINATION=0.25
    COEFFICIENT_LAIT_PAR_NOURRITURE : dict[TypeNourriture, float]={
        TypeNourriture.MARGUERITE:1.0,
        TypeNourriture.HERBE:0.8,
        TypeNourriture.FOIND:0.5,
        TypeNourriture.PAILLE:0.2,
        TypeNourriture.CEREALES:0.3
    } 
    Age_NAISSANCE=0

    def __init__(self, petitNom: str=None, poids: float=None):

        #Attribution des valeurs
        self.petitNom = petitNom
        self.poids = poids
        self.age = Vache.Age_NAISSANCE
        self.panse = 0.0 #initialisation de la panse à 0.0 pas obligé de mettre en parametre 
        
        #verification des valeurs initiales
        self._valid_etat()
    
    
    def _valid_etat(self) -> None:
        if( self.poids is  None or self.poids < self.POIDS_MIN or self.poids > self.POIDS_MAX):
            raise InvalidVacheException("Poids de la vache invalide")

        if( self.age is  None or self.age < 0 or self.age > self.AGE_MAX):
            raise InvalidVacheException("Âge de la vache invalide")
        
        if (self.petitNom.strip() == "" or self.petitNom is None):
            raise InvalidVacheException("Le petit nom de la vache ne peut pas être vide")

    
    def brouter( self, quantite:float,nourriture:any=None)-> None:
        if(quantite <= 0.0):
            raise InvalidVacheException("Quantité brouter doit être positive") 
        if(self.panse + quantite > self.PANSE_MAX):
            raise InvalidVacheException("Dépassement de la capacité de la panse")
        if( nourriture is not None):
            raise InvalidVacheException("Nourriture typée non autorisée")
        self.panse += quantite

    def ruminer(self)->None:
        if(self.panse<=0):
            raise InvalidVacheException("la panse de la vache est vide")
        gain= self.RENDEMENT_RUMINATION * self.panse
        self.poids+=gain
        self.panse=0.0

    def vieillir (self)->None:
        if(self.age >= self.AGE_MAX):
            raise InvalidVacheException("La vache a atteint l'age ")
        self.age +=1
        
        

    

    def _calculer_lait(self,panse_avant:float)->float:
        pass
    def _stocker_lait(self,lait_produit:float) ->None:
        pass
    def _post_rumination(self)->None:
        pass



