from vaches.vache import Vache
from vaches.exceptions import InvalidVacheException

class VacheALait(Vache):
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0

    def __init__(self,petitNom: str=None, poids: float=None):
        super().__init__(petitNom=petitNom, poids=poids)
        self.lait_disponible=0.0
        self.lait_total_produit=0.0
        self.lait_total_traite=0.0

    @property
    def get_lait_disponible(self) -> float:
        return self.lait_disponible
    @property
    def get_lait_total_produit(self) -> float: return self.lait_total_produit
    @property
    def get_lait_total_traite(self) -> float: 
        return self.lait_total_traite
    def traire(self, litres:float) -> float:
            if(litres <= 0): 
                raise InvalidVacheException("La quantité de lait à traire doit être positive") 
            if(litres > self.lait_disponible): 
                raise InvalidVacheException("La quantité de lait à traire ne peut pas dépasser le lait disponible")
            self.lait_disponible -= litres
            self.lait_total_traite += litres
            return litres
    def _post_rumination(self,panse_avant) -> None: 
        lait_produit = panse_avant * self.RENDEMENT_LAIT
        if lait_produit + self.lait_disponible>self.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("la production ne dois pas dépasser la capacité maximal/ on peut plus stocker le lait produit ")
        self.lait_disponible += lait_produit
        self.lait_total_produit += lait_produit
