from vaches.vache import vache_a_lait
from exceptions.InvalidVacheException import InvalidVacheException

class Pie_Noire(Vache_a_lait): 
    def __init__(self, lait_disponible:float=None, lait_total_produit:float=None, laitTotalTraite:float=None, petitNom: str=None, poids: float=None, age: int=None):
        super().__init__(petitNom, poids)
        self.rations= 0.0

    def brouter(self,typenourriture:TypeNourriture,quantite:float)->None:
        if quantite < 0.0: raise InvalidVacheException("La quantité de nourriture brouter ne peut pas être négative")
        if self.panse + quantite > self.PANSE_MAX: raise InvalidVacheException("Dépassement de la capacité de la panse") 
        if typenourriture not in self._RENDEMENT_NOURRITURE: raise InvalidVacheException("Type de nourriture non autorisé pour cette vache") 
        self.panse += quantite
        self.rations += quantite * self._RENDEMENT_NOURRITURE[typenourriture]
        _RENDEMENT_NOURRITURE = { TypeNourriture.HERBE: 0.5, TypeNourriture.FOIN: 0.4,
        TypeNourriture.PAILLE: 0.2, TypeNourriture.CEREALES: 0.3, TypeNourriture.MARGUERITE: 1.0 }

    